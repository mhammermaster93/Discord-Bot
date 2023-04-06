import requests
import json
from keys import Keys

url = "https://api.thecatapi.com/v1/images/search?format=img&limit=1"

payload={}
headers = {
  'Content-Type': 'img',
  'x-api-key': Keys.cat_api

}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)




