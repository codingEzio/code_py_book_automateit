import requests

r = requests.get("https://api.ipify.org/")

print(f"Resp obj  : {r}")
print(f"Resp url  : {r.url}")

print(f"Resp text : {r.text}")
print(f"Resp byte : {r.content}")