import requests
from concurrent.futures import ThreadPoolExecutor, FIRST_COMPLETED, wait

class Fetcher:

  def __init__(self, baseUrl):
    self.BASE_URL = baseUrl
    self.token = ''

  def __makeRequest(self, path):
    print('GET', path)
    link = self.BASE_URL + path
    return requests.get(link, headers={'X-Access-Token': self.token}).json()

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

      for el in done:
        result = el.result()
        results.append(result)

        if 'link' in result and 'msg' not in result:
          links = result['link']
          for key in links:
            queue.add(executor.submit(self.__makeRequest, links[key]))

    return results
