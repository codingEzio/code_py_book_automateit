import requests

"""
	Official Doc
		http://docs.python-requests.org/en/master/user/quickstart/
		
	Example down below copied from
		https://stackoverflow.com/a/47007419
"""

url = 'http://www.google.com/blahblah'

try:
	r = requests.get(url, timeout=3)
	r.raise_for_status()
except requests.exceptions.HTTPError as errh:
	print("Http Error:", errh)
except requests.exceptions.ConnectionError as errc:
	print("Error Connecting:", errc)
except requests.exceptions.Timeout as errt:
	print("Timeout Error:", errt)
except requests.exceptions.RequestException as err:
	print("OOps: Something Else", err)
