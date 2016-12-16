import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!links'):
        await client.send_message(message.channel, 'Check out the useful-links channel to the left for all the basic resources needed for Bot programming.')
    elif message.content.startswith('!kappa'):
        await client.send_message(message.channel, 'Kappa raised')

client.run('MjU4OTYwNzU1NjA3NjAxMTUy.CzRBqA.fsBJYI9ZFzrlmJP57FYR6FdDifA')
