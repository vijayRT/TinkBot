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
            await client.send_message(message.channel, 'A tutorial to get you started on the basics of Lua: https://learnxinyminutes.com/docs/lua/')
        elif message.content.startswith('!forum'):
            await client.send_message(message.channel, 'Link to the Dota2Bots Valve Developer forum: http://dev.dota2.com/forumdisplay.php?f=497')
        elif message.content.startswith('!path'):
            await client.send_message(message.channel, 'The bot scripts can be found at: Steam/steamapps/common/dota 2 beta/game/dota/scripts/vscripts/')
        elif message.content.startswith('!abilities'):
            await client.send_message(message.channel, 'Link to Valve\'s documentation on abilities: dhttps://github.com/SteamDatabase/GameTracking-Dota2/blob/master/game/dota/pak01_dir/scripts/npc/npc_abilities.txt')
        elif message.content.startswith('!docs'):
            await client.send_message(message.channel, 'ModDota\'s documentation for Bot scripting: http://docs.moddota.com/lua_bots/')
        elif message.content.startswith('!help'):
            await client.send_message(message.channel, 'Here\'s a list of available commands that TinkBot can reply to: \n !links - Simple command to direct new users to the useful_links channel \n !git - Path to DotaBots GitHub repo \n !forum - Link to the Bot Scripting subforum on the official Dota 2 Dev channel \n !docs - Link to the ModDota Documentation on Bot Scripting  \n !path - Path to local Bot scripts directory \n !abilities - A link to Valve\'s documentation on inbuilt Ability names \n !items - Link to Valve\'s documentation on inbuilt Item names')
        elif message.content.startswith('!items'):
            await client.send_message(message.channel, 'Link to Valve\'s documentation on items: https://github.com/SteamDatabase/GameTracking-Dota2/blob/master/game/dota/pak01_dir/scripts/npc/items.txt')
        
        
client.run('MjU4OTYwNzU1NjA3NjAxMTUy.CzRBqA.fsBJYI9ZFzrlmJP57FYR6FdDifA')
