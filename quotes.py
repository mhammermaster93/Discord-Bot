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

def grab_quote():
    quote_page = "https://orthodoxchurchquotes.wordpress.com/"
    page = requests.get(quote_page)
    soup = BeautifulSoup(page.text, 'html.parser')
    articles = soup.find_all('article','entry tite', '_5pbx userContent')
    quotes = []
    for article in articles:
        text = article.text.strip()
        quotes.append(text)
    return random.choice(quotes)

quote = grab_quote()
print(quote)
    
    
    
    
    