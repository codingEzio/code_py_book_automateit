import requests
from pprint import pprint

payload = {'key1': 'val1'}

r = requests.post("http://httpbin.org/post", data=payload)

pprint(r.json())
