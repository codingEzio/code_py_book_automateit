import requests

param = {'q': 'codingEzio'}

r = requests.get('https://github.com/search', params=param)

print(f'Request URL: {r.url}')
