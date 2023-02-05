import os
import discord
import scrapetube
import json


async def announce_vid():
    videos = scrapetube.get_channel(f'UCEPeyXOw5LA_DyTu2U4-4Gg',
                                    limit=1,
                                    sort_by='newest')

    urls = []

    for video in tuple(videos):
        urls.append(video['navigationEndpoint']['commandMetadata']
                    ['webCommandMetadata']['url'])
                    
    with open('previous.txt', 'r') as f:
        f = f.read()

    #need to figure out how to grab JUST the url
    #use url JSON pathing

    #print(url)

    if urls[0] != f:
        with open('previous.txt', 'w') as f:
            f.write(urls[0])
        return 'https://youtube.com' + urls[0]
    else:
        print("no new videos")
        return 'None' #don't return anything. I don't want it to