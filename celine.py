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
	numberending = ''
	if membercount % 10 == 1:
		numberending = 'st'
	if membercount % 10 == 2:
		numberending = 'nd'
	if not membercount % 10 == 1 and not membercount % 10 == 2:
		numberending = 'th'
	await client.send_message(discord.Object(id=535598974980325386), 'Welcome <@'+str(member.id)+'> to the **Coding Helpcenter**. You are our**'+str(membercount)+''+str(numberending)+'** member! We appreciate your stay and hope that we can help you!')
	
@client.command(pass_context=True)
async def ican(ctx, userrole):
	availableroles = ['Java', 'C/C++/C#', 'Python', 'Visual Basic .NET', 'Perl', 'Ruby', 'Swift', 'HTML', 'PHP', 'CSS', 'Javascript']
	if ctx.message.channel == discord.Object(id=533784202039132170):
		if userrole in ctx.message.author.roles:
			await client.say('Whoops... Looks as if ou already have that role ^0^')
		if not userrole in availableroles:
			await client.say('That role doesn\'t exist >.< Try it again!')
		if userrole in availableroles and not role in ctx.message.author.roles:
			await client.add_roles(ctx.message.author, userrole)
			await client.say('**'+ctx.message.author.name+'**, successfully gave you the role `'+role+'`!')
		else:
			return
					 
client.run(os.getenv('Token'))
