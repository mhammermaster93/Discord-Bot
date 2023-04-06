import requests
import json
from keys import Keys

url = "https://api.thedogapi.com/v1/images/search?format=json&limit=1"

payload={}
headers = {
  'Content-Type': 'application/json',
  'x-api-key': Keys.dog_api

}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)



