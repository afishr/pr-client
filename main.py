import requests
import concurrent.futures

def makeRequest(path, token=''):
	BASE_URL = 'http://0.0.0.0:5000'
	link = BASE_URL + path
	return requests.get(link, headers={'X-Access-Token': token}).json()

accessToken = makeRequest('/register')['access_token']
links = makeRequest('/home', accessToken)['link']

with concurrent.futures.ThreadPoolExecutor() as executor:
	results = [executor.submit(makeRequest, links[key], accessToken) for key in links]

	for f in concurrent.futures.as_completed(results):
		print(f.result())
		print('_____________')
