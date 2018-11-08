import requests
import json

# ORDER: 001

BASE_URL = 'https://api.github.com'
LINK_URL = 'https://gist.github.com'

# Token geneerated on 'https://github.com/settings/tokens'
username = 'codingEzio'
api_token = 'f4b5e1d9857cab92fa062908559414e4f639d9fe'

header = {
	'X-Github-Username': '%s' % username,
	'Content-Type'     : 'application/json',
	'Authorization'    : 'token %s' % api_token,
}

url = '/gists'

data = {
	'description': 'The description for this gist',
	'public'     : True,
	'files'      : {
		'file1.txt': {
			'content': 'String file contents'
		}
	}
}

r = requests.post(
	'%s%s' % (BASE_URL, url),
	headers=header,
	data=json.dumps(data)
)

print(r.json()['url'])