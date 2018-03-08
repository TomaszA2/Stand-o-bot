import os
import discord
import asyncio
global str

client = discord.Client()
szukane="stand"

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.author != client.user:
        if message.author.nick != 'Joseph' and message.author.nick != 'Polnareff' and message.author.nick != 'Avdol' and message.author.nick != 'Iggy' and message.author.nick != 'Jotaro' and message.author.nick != 'Jokero':
            if szukane in message.content.lower():
                tmp = await client.send_message(message.channel, 'The enemy Stand has appeared!')

client.run(os.getenv('TOKEN'))
