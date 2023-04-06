from bs4 import BeautifulSoup
import requests
import datetime


x = datetime()
print(x)

URL = "https://www.oca.org/saints/lives"

r = requests.get(URL)
print(r.content)

soup = BeautifulSoup(r.content, 'html5lib')

quotes = [] #array will store quotes

x = soup.find('p', attrs = {'class':'description'})

for contents in x:
    print(x.prettify())