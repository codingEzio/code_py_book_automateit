import requests
import json

# ORDER: 004

BASE_URL = 'https://api.github.com'
LINK_URL = 'https://gist.github.com'

username = 'codingEzio'
api_token = 'f4b5e1d9857cab92fa062908559414e4f639d9fe'
gist_id = '6ef4a6379fc1420e5945d1dd204d62da'

header = {
	'X-Github-Username': '%s' % username,
	'Content-Type'     : 'application/json',
	'Authorization'    : 'token %s' % api_token,
}

# --- delete! ---

url = f'/gists/{gist_id}'

r = requests.delete(
	f'{BASE_URL}{url}',
	headers=header,
)