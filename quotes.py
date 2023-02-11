# from bs4 import BeautifulSoup
# import requests
# import random

# def grab_quote(text):
    
#     quote_page = "https://orthodoxchurchquotes.wordpress.com/"
#     page = requests.get(quote_page)
    
#     #Scrub a single quote
    
#     if page.text:
#         soup = BeautifulSoup(page.text, 'html.parser')
#         article = soup.find('article', attrs={'id':'post-2817'})

#         text = article.text.strip()
#         return text


import requests
import random
from bs4 import BeautifulSoup
    
# def grab_quote():
#     quote_page = "https://orthodoxchurchquotes.wordpress.com/"
#     page = requests.get(quote_page)
#     soup = BeautifulSoup(page.text, 'html.parser')
  
#     content = soup.find_all('div', attrs={'class': 'entry-content'})
  
#     quotes = []
#     for contents in content:
#         text = contents.text.strip().split("Share this:")[0]
#         author = contents.text.strip().split("+")[1].strip() if "+" in contents.text else ""
#         quotes.append(text + " **" + author + "**")
    
#     return random.choice(quotes)

# quote = grab_quote()
# print(quote)

import requests
import random
from bs4 import BeautifulSoup
    
def grab_quote():
    quote_page = "https://orthodoxchurchquotes.wordpress.com/"
    page = requests.get(quote_page)
    soup = BeautifulSoup(page.text, 'html.parser')
  
    content = soup.find_all('div', attrs={'class': 'entry-content'})
  
    quotes = []
    texts = []
    for contents in content[-1:]:
        text = contents.text.strip().split("Share this:",)[0]
        author = contents.text.strip().split("+")[1].strip()
        quotes.append(text)
        texts.append("**" + author + "**")
        return random.choice(quotes)
        print(quote)

quote = grab_quote()




    