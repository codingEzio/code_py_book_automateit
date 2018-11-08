import requests
import json
from pprint import pprint

# ORDER: 002

BASE_URL = 'https://api.github.com'
LINK_URL = 'https://gist.github.com'

# Token geneerated on 'https://github.com/settings/tokens'
username = 'codingEzio'
api_token = 'f4b5e1d9857cab92fa062908559414e4f639d9fe'

# Temporary, for now.
#   Cuz there might be multiple gists with the same content.
gist_id = '6ef4a6379fc1420e5945d1dd204d62da'

header = {
	'X-Github-Username': '%s' % username,
	'Content-Type'     : 'application/json',
	'Authorization'    : 'token %s' % api_token,
}

url = "/gists/%s" % gist_id

r = requests.get(f'{BASE_URL}{url}', headers=header)

pprint(r.json())