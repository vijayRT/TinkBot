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
    elif message.content.startswith('!git'):
        await client.send_message(message.channel, 'Link to the Dota2Bots Github repo: https://github.com/dota2bots/dota2bots')
    elif message.content.startswith('!tutorial'):
        await client.send_message(message.channel, 'https://learnxinyminutes.com/docs/lua/')
    elif message.content.startswith('!forum'):
        await client.send_message(message.channel, 'Link to the Dota2Bots Valve Developer forum: http://dev.dota2.com/forumdisplay.php?f=497&s=da47a81e396e733114a60a050ecb0c9d')
    elif message.content.startswith('!path'):
        await client.send_message(message.channel, 'The bot scripts can be found at: Steam/steamapps/common/dota 2 beta/game/dota/scripts/vscripts/')
    elif message.content.startswith('!abilities'):
        await client.send_message(message.channel, 'A list of all ability names: https://developer.valvesoftware.com/wiki/Dota_2_Workshop_Tools/Scripting/Built-In_Ability_Names')

        
client.run('MjU4OTYwNzU1NjA3NjAxMTUy.CzRBqA.fsBJYI9ZFzrlmJP57FYR6FdDifA')
