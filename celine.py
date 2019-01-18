import discord
from discord.ext import commands
import os
import random
import time

client = commands.Bot(command_prefix = '+')
client.remove_command('help')

@client.event
async def on_ready():
	await client.change_presence(game=discord.Game(name='out for requests!', type=3))
	print('Startup complete!')
	
@client.event
async def on_member_join(member):
	
	membercount = int(member.server.member_count)
	
	
	
	if membercount % 10 == 1:
		numberending = 'st'
		
	if membercount % 10 == 2:
		numberending = 'nd'
		
	if not membercount % 10 == 1 and not membercount % 10 == 2:
		numberending = 'th'
	
	await client.send_message(discord.Object(id='535598974980325386'), 'Welcome <@'+str(member.id)+'> to the **Coding Helpcenter**. You are our**'+str(membercount)+''+numberending'** member! We appreciate your stay and hope that we can help you!')
	
client.run(os.getenv('Token')
