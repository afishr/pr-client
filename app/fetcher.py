import time
import requests
from parser import Parser
from diskcache import Cache
from concurrent.futures import ThreadPoolExecutor, FIRST_COMPLETED, wait
import threading
from queue import Queue


class Fetcher:
  def __init__(self, base_url):
    self.cache = Cache('tmp/cache')

    self.visited = set()
    self.result = []
    self.queue = Queue()
    self.lock = threading.Lock()

    self.base_url = base_url
    self.auth_token = ''

  def __makeRequest(self, path):
    link = self.base_url + path

    if link in self.cache:
      response = self.cache[link]
    else:
      response = requests.get(
        link, headers={'X-Access-Token': self.auth_token})

    if response.headers.get('Content-Type') == 'application/json':
      self.cache[link] = response

      return response.json()
    else:
      raise ValueError(
        "Expected JSON but got something else: " + response.text)

  def __authenticate(self):
    self.auth_token = self.__makeRequest('/register')['access_token']

  def fetch(self, num_threads=6):
    self.__authenticate()
    links = self.__makeRequest('/home')['link']

    perfStart = time.perf_counter()

    for path in links.values():
      self.queue.put(path)

    threads = []
    for _ in range(num_threads):
      t = threading.Thread(target=self.worker)
      t.start()
      threads.append(t)

    self.queue.join()

    for _ in threads:
      self.queue.put(None)

    for t in threads:
      t.join()

    return self.result

  def worker(self):
    while True:
      path = self.queue.get()

      if path is None:
        break

      if path in self.visited:
        self.queue.task_done()

      with self.lock:
        self.visited.add(path)

      try:
        data = self.__makeRequest(path)

        with self.lock:
          self.result.append(self.parse(data))

        if 'link' in data and 'msg' not in data:
          for key in data['link']:
            self.queue.put(data['link'][key])

      finally:
        self.queue.task_done()

  def parse(self, raw):
    data = raw['data']

    if 'mime_type' in raw:
      mimeType = raw['mime_type']

      if mimeType == 'application/xml':
        return Parser.parseXML(data)
      elif mimeType == 'text/csv':
        return Parser.parseCSV(data)
      elif mimeType == 'application/x-yaml':
        return Parser.parseYAML(data)
    else:
      return Parser.parseJSON(data)
