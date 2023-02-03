import random
import discord
import os
from images import *
from help import *
from Announcements import *
from googleapiclient.discovery import build

intents = discord.Intents.default()
intents.messages = True
my_secret = os.environ['TOKEN']
client = discord.Client(intents=intents)


#registering an event
@client.event
#called when the bot is ready to be used
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    #checking if the user message came from the bot
    if message.author == client.user:
        return
    if message.content.startswith('$roll'):
        #send message to channel
        await message.channel.send(f'{str(random.randint(1,6))}')
    if message.content.startswith('$flip'):
        #send message to channel
        flip = coin_flip()
        await message.channel.send(flip)
    if message.content.startswith('$pearl'):
        #send message to channel
        image = get_random_image()
        await message.channel.send(file=discord.File(image))
    if message.content.startswith('$quote'):
        quote = get_quote()
        await message.channel.send(quote)
    if message.content.startswith('$video'):
        video = video_links()
        await message.channel.send(video)
    if message.content.startswith('$help'):
        await message.channel.send(write_help())

    #make bot post in different channel
    if message.content.startswith('$test'):
        channel = client.get_channel(1070887941406195753)
        await channel.send("hello")


#update_help()
client.run(my_secret)
