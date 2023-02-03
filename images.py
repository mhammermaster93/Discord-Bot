import random
import scrapetube

pics = [
    'pics/1.jpg',
    'pics/2.jpg',
    'pics/3.jpg',
    'pics/4.jpg',
    'pics/5.jpg',
    'pics/6.jpg',
    'pics/7.jpg',
    'pics/8.jpg',
    'pics/9.jpg'
]

def get_random_image():
    return random.choice(pics)


def video_links():
  channels = ['UChozbOPP6uOJ2UkiTZy-sgQ','UCkpBmkoZ6yToHhB8uFDp46Q','UCEPeyXOw5LA_DyTu2U4-4Gg','UCCdAuHh5MlTXQPxts1W9ICw',''
             ]
 
  videos = scrapetube.get_channel(f'{random.choice(channels)}',limit = 20, sort_by = 'popular')

  urls = []

  for video in videos:
   urls.append('https://youtube.com' + video['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url'])

  randon_url = random.choice(urls)

  return randon_url

#print(video_links())

def coin_flip():
  flip = int(random.randint(1,2))
  if flip == 1:
    return 'heads'
  elif flip == 2:
    return 'tails'