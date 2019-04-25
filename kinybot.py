import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import platform
import colorsys
import random
import os
import time
import sys
import warnings
import logging
import asyncio
import re
import json
import traceback
import termcolor
import discord.ext.commands
from discord.ext.commands.errors import *
import core.blame
import core.keystore
import core.settings
import utils
from queuedict import QueueDict
from modules.reporter import report
from advertising import AdvertisingMixin
from patrons import PatronageMixin
from discord.voice_client import VoiceClient
from discord import Game, Embed, Color, Status, ChannelType

client = commands.Bot(command_prefix=';')
ivan='445198123837554688'
start=time.time()

@client.event
async def on_ready():
	print('Bot is online.')
	print(client.user.name)
	print(client.user.id)
	await client.change_presence(game=discord.Game(name='http://kinysite.weebly.com || ;help',type=0))
	
@client.command()
async def ping():
	await client.say(':ping_pong:')
	await client.say('**You pinged me haha**')
	
@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def warn(ctx, userName: discord.User, *, message:str): 
    await client.send_message(userName, "You have been warned for: **{}**".format(message))
    await client.say(":warning: __**{0} Has Been Warned!**__ :warning: ** Reason:{1}** ".format(userName,message))
    pass
	
@client.command()
async def invite():
	await client.say(':gift:')
	await client.say('https://discordapp.com/api/oauth2/authorize?client_id=559760760914313218&permissions=8&scope=bot')
	
@client.command()
async def google():
	await client.say(':envelope:')
	await client.say('https://www.google.com')
	
@client.command()
async def porn():
	await client.say(':underage:')
	await client.say('https://www.pornhub.com')
	
@client.command()
async def support():
	await client.say('https://discord.gg/sxNAB3e')
	await client.say('**Support group for bugs in bot!**')
		
@client.command()
async def twitch():
	await client.say(':mouse_three_button:')
	await client.say('https://twitch.tv')
	
@client.command()
async def youtube():
	await client.say(':camera:')
	await client.say('https://youtube.com')
	
@client.command()
async def tenorgif():
	await client.say(':horse:')
	await client.say('https://tenor.com')
	
@client.command()
async def filmi2k():
	await client.say(':film_frames:')
	await client.say('https://filmi2k.com')
	
	
@client.command()
async def new():
	await client.say(':confetti_ball:')
	await client.say('``1.04.2019`` | **New prefix ";" | New command-userinfo,membercount,embed,serverinfo,clear |  Enjoy**')
	
@client.command(pass_context=True)
async def uptime(ctx):
	now=time.time()
	sec=int(now-start)
	mins=int(sec//60)
	await client.say(f'**Uptime is {sec} seconds!**')
	
@client.command(pass_context=True)
async def presence(ctx,text:str,type:int):
	if ctx.message.author.id==(ivan):
		await client.change_presence(game=discord.Game(name=text,type=type))
	else:
			await client.say('**No permissions!**')
			
@client.command()
async def website():
	await client.say(':inbox_tray:')
	await client.say('http://kinysite.weebly.com')
	
@client.command()
async def partnership():
	await client.say(':trophy:')
	await client.say('``To be a partner with us, you must have a group of at least 50-100 people in it``')
	
@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)     
async def userinfo(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="``ID``", value=user.id, inline=True)
    embed.add_field(name="``Status``", value=user.status, inline=True)
    embed.add_field(name="``Highest role``", value=user.top_role)
    embed.add_field(name="``Joined``", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await client.say(embed=embed)
    
@client.command(pass_context=True, aliases=['server'])
@commands.has_permissions(kick_members=True)
async def membercount(ctx, *args):
    """
    Shows stats and information about current guild.
    ATTENTION: Please only use this on your own guilds or with explicit
    permissions of the guilds administrators!
    """
    if ctx.message.channel.is_private:
        await client.delete_message(ctx.message)
        return

    g = ctx.message.server

    gid = g.id
    membs = str(len(g.members))
    membs_on = str(len([m for m in g.members if not m.status == Status.offline]))
    users = str(len([m for m in g.members if not m.bot]))
    users_on = str(len([m for m in g.members if not m.bot and not m.status == Status.offline]))
    bots = str(len([m for m in g.members if m.bot]))
    bots_on = str(len([m for m in g.members if m.bot and not m.status == Status.offline]))
    created = str(g.created_at)
    
    em = Embed(title="Membercount")
    em.description =    "```\n" \
                        "Members:   %s (%s)\n" \
                        "  Users:   %s (%s)\n" \
                        "  Bots:    %s (%s)\n" \
                        "Created:   %s\n" \
                        "```" % (membs, membs_on, users, users_on, bots, bots_on, created)

    await client.send_message(ctx.message.channel, embed=em)
    await client.delete_message(ctx.message)
    
@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def embed(ctx, *args):
    """
    Sending embeded messages with color (and maby later title, footer and fields)
    """
    argstr = " ".join(args)
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    text = argstr
    color = discord.Color((r << 16) + (g << 8) + b)
    await client.send_message(ctx.message.channel, embed=Embed(color = color, description=text))
    
@client.command(pass_context=True)  
@commands.has_permissions(kick_members=True)     

async def serverinfo(ctx):
    '''Displays Info About The Server!'''

    server = ctx.message.server
    roles = [x.name for x in server.role_hierarchy]
    role_length = len(roles)

    if role_length > 50: #Just in case there are too many roles...
        roles = roles[:50]
        roles.append('>>>> Displaying[50/%s] Roles'%len(roles))

    roles = ', '.join(roles);
    channelz = len(server.channels);
    time = str(server.created_at); time = time.split(' '); time= time[0];
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    join = discord.Embed(description= '%s '%(str(server)),title = 'Server Name', color = discord.Color((r << 16) + (g << 8) + b));
    join.set_thumbnail(url = server.icon_url);
    join.add_field(name = '__Owner__', value = str(server.owner) + '\n' + server.owner.id);
    join.add_field(name = '__ID__', value = str(server.id))
    join.add_field(name = '__Member Count__', value = str(server.member_count));
    join.add_field(name = '__Text/Voice Channels__', value = str(channelz));
    join.add_field(name = '__Roles (%s)__'%str(role_length), value = roles);
    join.set_footer(text ='Created: %s'%time);

    return await client.say(embed = join);
    
@client.command(pass_context = True)
@commands.has_permissions(manage_messages=True)  
async def clear(ctx, number):
 
    if ctx.message.author.server_permissions.manage_messages:
         mgs = [] #Empty list to put all the messages in the log
         number = int(number) #Converting the amount of messages to delete to an integer
    async for x in client.logs_from(ctx.message.channel, limit = number+1):
        mgs.append(x)            
       
    try:
        await client.delete_messages(mgs)          
        await client.say(str(number)+' messages deleted')
     
    except discord.Forbidden:
        await client.say(embed=Forbidden)
        return
    except discord.HTTPException:
        await client.say('clear failed.')
        return         
   
 
    await client.delete_messages(mgs)
    
@client.command(pass_context=True)
async def poll(ctx, question, *options: str):
        if len(options) <= 1:
            await client.say('``You need more than one option to make a poll!``')
            return
        if len(options) > 10:
            await client.say('``You cannot make a poll for more than 10 things!``')
            return

        if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
            reactions = ['👍', '👎']
        else:
            reactions = ['1\u20e3', '2\u20e3', '3\u20e3', '4\u20e3', '5\u20e3', '6\u20e3', '7\u20e3', '8\u20e3', '9\u20e3', '\U0001f51f']

        description = []
        for x, option in enumerate(options):
            description += '\n {} {}'.format(reactions[x], option)
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title=question, description=''.join(description), color = discord.Color((r << 16) + (g << 8) + b))
        react_message = await client.say(embed=embed)
        for reaction in reactions[:len(options)]:
            await client.add_reaction(react_message, reaction)
        embed.set_footer(text='Poll ID: {}'.format(react_message.id))
        await client.edit_message(react_message, embed=embed)

@client.command(pass_context=True)
async def guess(ctx, number):
    try:
        arg = random.randint(1, 10)
    except ValueError:
        await client.say("``Invalid number``")
    else:
        await client.say('The correct answer is ' + str(arg))

@client.group()
async def calculator():
    pass
    
@calculator.command(pass_context=True)
async def add(ctx, a: int, b:int):
    await client.say(a+b)
    
@calculator.command(pass_context=True)
async def subtract(ctx, a: int, b:int):
    await client.say(a-b)
    
@calculator.command(pass_context=True)
async def multiply(ctx, a: int, b:int):
    await client.say(a*b)
    
@calculator.command(pass_context=True)
async def divide(ctx, a: int, b:int):
    await client.say(a/b)
	
client.run(os.getenv('Token'))
