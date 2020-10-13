import requests
import concurrent.futures

class Fetcher():
	
	def __init__(self, baseUrl):
		self.BASE_URL = baseUrl
		self.token = ''

	def __makeRequest(self, path):
		link = self.BASE_URL + path
		return requests.get(link, headers={'X-Access-Token': self.token}).json()
	
	def __authenticate(self):
		self.token = self.__makeRequest('/register')['access_token']

	def fetch(self):
		self.__authenticate()
		links = self.__makeRequest('/home')['link']

		with concurrent.futures.ThreadPoolExecutor() as executor:
			queue = [executor.submit(self.__makeRequest, links[key]) for key in sorted(links.keys(), reverse=True)]
			results = []

			while queue:
				response = queue.pop().result()
				results.append(response)

				if 'link' in response and 'msg' not in response:
					links = response['link']
					for key in links:
						queue.append(executor.submit(self.__makeRequest, links[key]))
		
		return results