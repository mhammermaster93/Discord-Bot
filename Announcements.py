import os
import discord
import scrapetube
import json


# def video_links():
#   channels = ['UChozbOPP6uOJ2UkiTZy-sgQ','UCkpBmkoZ6yToHhB8uFDp46Q','UCEPeyXOw5LA_DyTu2U4-4Gg','UCCdAuHh5MlTXQPxts1W9ICw',''
#              ]

#   videos = scrapetube.get_channel(f'{random.choice(channels)}',limit = 20, sort_by = 'popular')

#   urls = []

#   for video in videos:
#    urls.append('https://youtube.com' + video['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url'])

#   randon_url = random.choice(urls)

#   return randon_url

# #print(video_links())
async def announce_vid():
    videos = scrapetube.get_channel(f'UCEPeyXOw5LA_DyTu2U4-4Gg',
                                    limit=1,
                                    sort_by='newest')

    urls = []

    for video in tuple(videos):
        urls.append(video['navigationEndpoint']['commandMetadata']
                    ['webCommandMetadata']['url'])
    print(urls)

    with open('previous.txt', 'r') as f:
        f = f.read()

    #need to figure out how to grab JUST the url
    #use url JSON pathing

    #print(url)

    if urls[0] != f:
        return 'https://youtube.com' + urls[0]
    else:
        with open('previous.txt', 'w') as f:
            f.write(urls[0])
        return "no new videos"
