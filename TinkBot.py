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
    if message.author != 'TinkBot#5973':
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
        elif message.content.startswith('!docs'):
            await client.send_message(message.channel, 'ModDota\'s documentation for Bot scripting: http://docs.moddota.com/lua_bots/')
        elif message.content.startswith('!help'):
            await client.send_message(message.channel, 'Here\'s a list of available commands that TinkBot can reply to: \n !links - Simple command to direct new users to the useful_links channel \n !git - Path to DotaBots GitHub repo \n !abilities - A link to Valve\'s documentation on inbuilt Ability names \n !path - Path to local Bot scripts directory \n !forum - Link to the Bot Scripting subforum on the official Dota 2 Dev channel \n !docs - Link to the ModDota Documentation on Bot Scripting')

        
client.run('MjU4OTYwNzU1NjA3NjAxMTUy.CzRBqA.fsBJYI9ZFzrlmJP57FYR6FdDifA')
