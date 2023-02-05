import random
import discord
from urllib.request import *
from urllib.error import *
from discord.ext import tasks, commands
from images import video_links, coin_flip, get_random_image
from help import get_quote, write_help
from Announcements import announce_vid
from dotenv import load_dotenv
from quotes import *

load_dotenv()

try:
    intents = discord.Intents.all()
    intents.messages = True
    client = discord.Client(intents=intents)

    #registering an event
    @client.event
    #called when the bot is ready to be used
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))

        update_new_video.start()
    
    @tasks.loop(seconds=5)
    async def update_new_video():
        video = await announce_vid()
        if video != 'None':
            channel = client.get_channel(1070887941406195753)
            await channel.send(video)
            


    @client.event
    async def on_message(message):
        #checking if the user message came from the bot
        if message.author == client.user:
            return
        if message.content.startswith('$roll'):
            #send message to channel
            await message.channel.send(f'{str(random.randint(1,6))}')
        if message.content.startswith('$ping'):
            #send message to channel
            await message.channel.send(f'{round(client.latency * 1000)}ms')
        if message.content.startswith('$flip'):
            #send message to channel
            flip = coin_flip()
            await message.channel.send(flip)
        if message.content.startswith('$pearl'):
            #send message to channel
            image = get_random_image()
            await message.channel.send(file=discord.File(image))
        if message.content.startswith('$quote'):
            quote = grab_quote()
            await message.channel.send(quote)
        if message.content.startswith('$video'):
            video = video_links()
            await message.channel.send(video)
        if message.content.startswith('$help'):
            await message.channel.send(write_help())
        #make bot post in different channel
        if message.content.startswith('$test'):
            channel = client.get_channel(1070887941406195753)
            video = await announce_vid()
            await channel.send(video)
        if message.content.startswith('$hello'):
            statement = "I am a bot created by apostalyptic for the purposes of helping father Mikhail. I am a gift."
            await message.channel.send(statement)
    client.run(TOKEN)
except Exception as e:
    print(e)

#Joshua add token back