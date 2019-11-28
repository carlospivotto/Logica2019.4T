# https://swapi.co/api/people/1 

import requests
import json 

for i in range(1000):
  response = requests.get(f"https://swapi.co/api/people/{i+1}")

  status = response.status_code 

  if status == 200:
    personagem = json.loads(response.text)
    print(personagem["name"])


