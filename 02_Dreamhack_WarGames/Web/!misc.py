import requests

url = "http://host3.dreamhack.games:16727/"

res = requests.head(url)

print(res.headers)
