import discord
import asyncio
global str

client = discord.Client()
szukane="stand"
znaleziono=0

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.author != client.user:
        if szukane in message.content.lower():
            tmp = await client.send_message(message.channel, 'The enemy Stand has appeared!')

client.run('NDA2Nzk0NDcwNzg1NTQ4Mjg4.DU4QWw.bJ56iFS8qdgRllGNVuYvSGyRgM0')
