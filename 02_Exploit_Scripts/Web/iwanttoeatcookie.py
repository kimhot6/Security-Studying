import requests

url = 'http://host8.dreamhack.games:12668/c1'

headers = {
  'X-Method-Override': 'POST'
}

res = requests.head(url)
print(res.cookies)
