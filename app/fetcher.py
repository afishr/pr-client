import time
import requests
from parser import Parser
from diskcache import Cache
from concurrent.futures import ThreadPoolExecutor, FIRST_COMPLETED, wait


class Fetcher:
  def __init__(self, store):
    self.store = store
    self.cache = Cache('tmp/cache')

  def __makeRequest(self, base, path, token=''):
    link = base + path

    if link in self.cache:
      response = self.cache[link]
    else:
      response = requests.get(link, headers={'X-Access-Token': token})

    if response.headers.get('Content-Type') == 'application/json':
      self.cache[link] = response

      return response.json()
    else:
      raise ValueError(
        "Expected JSON but got something else: " + response.text)

  def __authenticate(self, base):
    return self.__makeRequest(base, '/register')['access_token']

  def fetch(self, base):
    token = self.__authenticate(base)
    links = self.__makeRequest(base, '/home', token=token)['link']

    executor = ThreadPoolExecutor(max_workers=6)
    queue = [executor.submit(self.__makeRequest, base,
                             links[key], token) for key in links]

    perfStart = time.perf_counter()

    while queue:
      done, queue = wait(queue, return_when=FIRST_COMPLETED)

      for future in done:
        result = future.result()
        self.processAndSave(result)

        if 'link' in result and 'msg' not in result:
          links = result['link']
          for key in links:
            queue.add(executor.submit(
              self.__makeRequest, base, links[key], token))

    perfEnd = time.perf_counter()
    print(f"Fetch time: {perfEnd - perfStart:.4f} seconds")

  def processAndSave(self, raw):
    data = raw['data']

    if 'mime_type' in raw:
      mimeType = raw['mime_type']

      if mimeType == 'application/xml':
        self.store.adds(Parser.parseXML(data))
      elif mimeType == 'text/csv':
        self.store.adds(Parser.parseCSV(data))
      elif mimeType == 'application/x-yaml':
        self.store.adds(Parser.parseYAML(data))
    else:
      self.store.adds(Parser.parseJSON(data))
