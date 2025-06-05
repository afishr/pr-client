import requests
from diskcache import Cache
from concurrent.futures import ThreadPoolExecutor, FIRST_COMPLETED, wait


class Fetcher:

  def __init__(self, baseUrl):
    self.BASE_URL = baseUrl
    self.token = ''
    self.cache = Cache('./tmp/cache/')

  def __makeRequest(self, path):
    link = self.BASE_URL + path

    if link in self.cache:
      response = self.cache[link]
    else:
      response = requests.get(link, headers={'X-Access-Token': self.token})

    if response.headers.get('Content-Type') == 'application/json':
      self.cache[link] = response

      return response.json()
    else:
      raise ValueError(
        "Expected JSON but got something else: " + response.text)

  def __authenticate(self):
    self.token = self.__makeRequest('/register')['access_token']

  def fetch(self):
    self.__authenticate()
    links = self.__makeRequest('/home')['link']

    executor = ThreadPoolExecutor(max_workers=6)
    queue = [executor.submit(self.__makeRequest, links[key]) for key in links]
    results = []

    while queue:
      done, queue = wait(queue, return_when=FIRST_COMPLETED)

      for future in done:
        result = future.result()
        results.append(result)

        if 'link' in result and 'msg' not in result:
          links = result['link']
          for key in links:
            queue.add(executor.submit(self.__makeRequest, links[key]))

    return results
