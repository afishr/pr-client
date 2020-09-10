import requests

BASE_URL = 'http://0.0.0.0:5000'

def makeRequest(path, token=''):
	return requests.get(path, headers={'X-Access-Token': token}).json()

accessToken = makeRequest(BASE_URL + '/register')['access_token']
links = makeRequest(BASE_URL + '/home', accessToken)['link']

for key in links:
	link = links[key]

	print(makeRequest(BASE_URL + link, accessToken))
