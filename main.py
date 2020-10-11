import requests
import concurrent.futures

def makeRequest(path, token=''):
	print('GET ' + path)
	BASE_URL = 'http://0.0.0.0:5000'
	link = BASE_URL + path
	return requests.get(link, headers={'X-Access-Token': token}).json()

accessToken = makeRequest('/register')['access_token']
links = makeRequest('/home', accessToken)['link']

with concurrent.futures.ThreadPoolExecutor() as executor:
	queue = [executor.submit(makeRequest, links[key], accessToken) for key in links]
	results = []

	while queue:
		response = queue.pop(0).result()
		results.append(response)

		if 'link' in response and 'msg' not in response:
			links = response['link']
			for key in links:
				queue.append(executor.submit(makeRequest, links[key], accessToken))

print(results)
