import discord
import os
import crawler
from keep_alive import keep_alive

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
        letterNum = li[1]
        sectionNum = li[2]
            await message.channel.send(crawler.retrieveSectionBySectionNumber(letterNum, sectionNum))

keep_alive()

client.run(os.environ['TOKEN'])
