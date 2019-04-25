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
	
warnings.simplefilter('default')
logging.basicConfig(level = logging.INFO)
sys.setrecursionlimit(2500)


REQUIRED_PERMISSIONS_MESSAGE = '''\
The bot does not have all the permissions it requires in order to run in this channel. It requires the following permissions:
 - Add reactions
 - Attach files
 - Embed links
 - Read message history
Contact your server administrators to rectify this problem.
You can seek additional support on the official mathbot server: https://discord.gg/JbJbRZS
'''


class MathBot(AdvertisingMixin, PatronageMixin, discord.ext.commands.AutoShardedBot):

	def __init__(self, parameters):
		super().__init__(
			command_prefix=_determine_prefix,
			pm_help=True,
			shard_count=parameters.get('shards total'),
			shard_ids=parameters.get('shards mine'),
			max_messages=2000,
			fetch_offline_members=False
		)
		self.parameters = parameters
		self.release = parameters.get('release')
		self.keystore = _create_keystore(parameters)
		self.settings = core.settings.Settings(self.keystore)
		self.command_output_map = QueueDict(timeout = 60 * 10) # 10 minute timeout
		assert self.release in ['development', 'beta', 'release']
		self.remove_command('help')
		for i in _get_extensions(parameters):
			self.load_extension(i)

	def run(self):
		super().run(self.parameters.get('token'))

	async def on_message(self, message):
		if self.release != 'production' or not message.author.bot:
			if utils.is_private(message.channel) or self._can_post_in_guild(message):
				context = await self.get_context(message)
				perms = context.message.channel.permissions_for(context.me)
				required = [
					perms.add_reactions,
					perms.attach_files,
					perms.embed_links,
					perms.read_message_history,
				]
				if not context.valid:
					self.dispatch('message_discarded', message)
				elif not all(required):
					await message.channel.send(REQUIRED_PERMISSIONS_MESSAGE)
				else:
					context.send = self.send_patch(message, context.send)
					await self.invoke(context)

	def send_patch(self, invoker, original):
		async def send(*args, **kwargs):
			sent = await original(*args, **kwargs)
			await core.blame.set_blame(self.keystore, sent, invoker.author)
			self.message_link(invoker, sent)
			return sent
		return send

	def _can_post_in_guild(self, message):
		if message.channel is None:
			return False
		perms = message.channel.permissions_for(message.guild.me)
		return perms.read_messages and perms.send_messages

	# Enabling this will cause output to be deleted with the coresponding
	# commands are deleted.
	# async def on_message_delete(self, message):
	# 	to_delete = self.command_output_map.pop(message.id, [])
	# 	await self._delete_messages(to_delete)

	# Using this, it's possible to edit a tex message
	# into some other command, so I might add some additional
	# restrictions to this later.
	async def on_message_edit(self, before, after):
		if before.content != after.content:
			to_delete = self.command_output_map.pop(before.id, [])
			await asyncio.gather(
				self._delete_messages(to_delete),
				self.on_message(after)
			)

	async def _delete_messages(self, messages):
		for i in messages:
			try:
				await i.delete()
			except (discord.errors.Forbidden, discord.errors.NotFound):
				pass
			await asyncio.sleep(2)

	def message_link(self, invoker, sent):
		lst = self.command_output_map.get(invoker.id, default=[])
		self.command_output_map[invoker.id] = lst + [sent]

	async def on_error(self, event, *args, **kwargs):
		_, error, _ = sys.exc_info()
		if event in ['message', 'on_message', 'message_discarded', 'on_message_discarded', 'on_command_error']:
			msg = f'**Error while handling a message**'
			await self.handle_contextual_error(args[0].channel, error, msg)
		else:
			termcolor.cprint(traceback.format_exc(), 'blue')
			await self.report_error(None, error, f'An error occurred during and event and was not reported: {event}')

	async def on_command_error(self, context, error):
		details = f'**Error while running command**\n```\n{context.message.clean_content}\n```'
		await self.handle_contextual_error(context, error, details)

	async def handle_contextual_error(self, destination, error, human_details=''):
		if isinstance(error, CommandNotFound):
			pass # Ignore unfound commands
		elif isinstance(error, MissingRequiredArgument):
			await destination.send(f'Argument {error.param} required.')
		elif isinstance(error, TooManyArguments):
			await destination.send(f'Too many arguments given.')
		elif isinstance(error, BadArgument):
			await destination.send(f'Bad argument: {error}')
		elif isinstance(error, NoPrivateMessage):
			await destination.send(f'That command cannot be used in DMs.')
		elif isinstance(error, MissingPermissions):
			await destination.send(f'You are missing the following permissions required to run the command: {", ".join(error.missing_perms)}.')
		elif isinstance(error, core.settings.DisabledCommandByServerOwner):
			await destination.send(embed=discord.Embed(
				title='Command disabled',
				description=f'The sever owner has disabled that command in this location.',
				colour=discord.Colour.orange()
			))
		elif isinstance(error, DisabledCommand):
			await destination.send(embed=discord.Embed(
				title='Command globally disabled',
				description=f'That command is currently disabled. Either it relates to an unreleased feature or is undergoing maintaiance.',
				colour=discord.Colour.orange()
			))
		elif isinstance(error, CommandInvokeError):
			await self.report_error(destination, error.original, human_details)
		else:
			await self.report_error(destination, error, human_details)

	async def report_error(self, destination, error, human_details):
		tb = ''.join(traceback.format_exception(etype=type(error), value=error, tb=error.__traceback__))
		termcolor.cprint(human_details, 'red')
		termcolor.cprint(tb, 'blue')
		try:
			if destination is not None:
				embed = discord.Embed(
					title='An internal error occurred.',
					colour=discord.Colour.red(),
					description='A report has been automatically sent to the developer. If you wish to follow up, or seek additional assistance, you may do so at the mathbot server: https://discord.gg/JbJbRZS'
				)
				await destination.send(embed=embed)
		finally:
			await report(self, f'{self.shard_ids} {human_details}\n```\n{tb}\n```')


def run(parameters):
	if sys.getrecursionlimit() < 2500:
		sys.setrecursionlimit(2500)
	MathBot(parameters).run()


@utils.listify
def _get_extensions(parameters):
	yield 'modules.about'
	yield 'modules.blame'
	yield 'modules.calcmod'
	yield 'modules.dice'
	# yield 'modules.greeter'
	yield 'modules.heartbeat'
	yield 'modules.help'
	yield 'modules.latex'
	yield 'modules.purge'
	yield 'modules.reporter'
	yield 'modules.settings'
	yield 'modules.wolfram'
	yield 'modules.reboot'
	yield 'modules.oeis'
	if parameters.get('release') == 'development':
		yield 'modules.echo'
		yield 'modules.throws'
	yield 'patrons' # This is a little weird.
	if parameters.get('release') == 'release':
		yield 'modules.analytics'


def _create_keystore(parameters):
	keystore_mode = parameters.get('keystore mode')
	if keystore_mode == 'redis':
		return core.keystore.create_redis(
			parameters.get('keystore redis url'),
			parameters.get('keystore redis number')
		)
	if keystore_mode == 'disk':
		return core.keystore.create_disk(parameters.get('keystore disk filename'))
	raise ValueError(f'"{keystore_mode}" is not a valid keystore mode')


async def _determine_prefix(bot, message):
	if message.guild is None:
		prefixes = ['= ', '=', '']
	else:
		custom = str(await bot.settings.get_server_prefix(message))
		prefixes = [custom + ' ', custom]
	return discord.ext.commands.when_mentioned_or(*prefixes)(bot, message)


if __name__ == '__main__':
	
client.run(os.getenv('Token'))
