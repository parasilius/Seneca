import discord
import os
import database
from keep_alive import keep_alive
from random import randint

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$letter'):
        li = list(message.content.split())
        if li[1] == 'random':
            letterNum = randint(1, 124)
        else:
            letterNum = li[1]
        if len(li) == 3:
            sectionNum = li[2]
            await message.channel.send(database.retrieveSection(letterNum, sectionNum))
        if len(li) == 2:
            sectionNum = 1
            while True:
                try:
                    await message.channel.send(database.retrieveSection(letterNum, sectionNum))
                    sectionNum += 1
                except:
                    break

keep_alive()

client.run(os.environ['TOKEN'])
