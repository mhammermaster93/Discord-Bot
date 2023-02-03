import random
import scrapetube

def scrape_url():
  lo = "UCCdAuHh5MlTXQPxts1W9ICw"




def video_links():
  channels = ['UChozbOPP6uOJ2UkiTZy-sgQ','UCkpBmkoZ6yToHhB8uFDp46Q','UCEPeyXOw5LA_DyTu2U4-4Gg','UCCdAuHh5MlTXQPxts1W9ICw',''
             ]
 
  videos = scrapetube.get_channel(f'{random.choice(channels)}',limit = 20, sort_by = 'popular')

  urls = []

  for video in videos:
   urls.append('https://youtube.com' + video['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url'])

  randon_url = random.choice(urls)

  return randon_url