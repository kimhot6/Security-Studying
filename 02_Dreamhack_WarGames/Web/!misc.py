import requests

url = "http://host3.dreamhack.games:20925/flag"

data = {
  'key' : '409ac0d96943d3da52f176ae9ff2b974'
  # 'cmd_input' : "sleep 6"
}

res = requests.post(url, data=data)

print(res.text)
