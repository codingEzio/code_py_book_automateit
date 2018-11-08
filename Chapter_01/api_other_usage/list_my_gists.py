import requests

BASE_URL = 'https://api.github.com'
LINK_URL = 'https://gist.github.com'

username = 'codingEzio'
api_token = 'f4b5e1d9857cab92fa062908559414e4f639d9fe'

header = {
	'X-Github-Username': '%s' % username,
	'Content-Type'     : 'application/json',
	'Authorization'    : 'token %s' % api_token,
}

url = f"/users/{username}/gists"
r = requests.get(
	f'{BASE_URL}{url}',
	headers=header
)

gists = r.json()

for gist in gists:
	print(
		gist['id'],
		gist['url'],
		sep='\n\t'
	)