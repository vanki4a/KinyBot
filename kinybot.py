import discord
from discord.ext import commands
import asyncio
import time

bot = commands.Bot(command_prefix=';')
ivan='445198123837554688'
start=time.time()

@bot.event
async def on_ready():
	print('Bot is online.')
	print(bot.user.name)
	print(bot.user.id)
	await bot.change_presence(game=discord.Game(name=';help',type=3))
	
@bot.command()
async def ping():
	await bot.say(':ping_pong:')
	await bot.say('**You pinged me haha**')
	
@bot.command(pass_context=True)
async def warn(ctx,target:discord.Member): 
    if ctx.message.author.id==(ivan):
      await bot.send_message(target,'**Warning!**')
    else:
     	await bot.say('**No permissions!**')
	
@bot.command()
async def invite():
	await bot.say(':gift:')
	await bot.say('https://discordapp.com/api/oauth2/authorize?client_id=559760760914313218&permissions=8&scope=bot')
	
@bot.command()
async def google():
	await bot.say(':envelope:')
	await bot.say('https://www.google.com')
	
@bot.command()
async def porn():
	await bot.say(':underage:')
	await bot.say('https://www.pornhub.com')
	
@bot.command()
async def support():
	await bot.say('https://discord.gg/sxNAB3e')
	await bot.say('**Support group for bugs in bot!**')
	
	
@bot.command()
async def twitch():
	await bot.say(':mouse_three_button:')
	await bot.say('https://twitch.tv')
	
@bot.command()
async def youtube():
	await bot.say(':camera:')
	await bot.say('https://youtube.com')
	
@bot.command()
async def tenorgif():
	await bot.say(':horse:')
	await bot.say('https://tenor.com')
	
@bot.command()
async def filmi2k():
	await bot.say(':film_frames:')
	await bot.say('https://filmi2k.com')
	
@bot.command()
async def bug():
	await bot.say(':rotating_light:')
	await bot.say('**You bug my system :(**')
	
@bot.command()
async def hack():
	await bot.say('**Haha I hack you,now I delete your account!** **(kappa123)** :smile:')
	
@bot.command()
async def new():
	await bot.say(':confetti_ball:')
	await bot.say('``1.04.2019`` | **New prefix ";" | Enjoy**')
	
@bot.command(pass_context=True)
async def uptime(ctx):
	now=time.time()
	sec=int(now-start)
	mins=int(sec//60)
	await bot.say(f'**Uptime is {sec} seconds!**')
	
@bot.command(pass_context=True)
async def presence(ctx,text:str,type:int):
	if ctx.message.author.id==(ivan):
		await bot.change_presence(game=discord.Game(name=text,type=type))
	else:
			await bot.say('**No permissions!**')
			
@bot.command()
async def website():
	await bot.say(':inbox_tray:')
	await bot.say('http://kinysite.weebly.com')
	
@bot.command()
async def partnership():
	await bot.say(':trophy:')
	await bot.say('``To be a partner with us, you must have a group of at least 50-100 people in it``')
  
  client.run(os.getenv('Token'))
