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
	await client.send_message(discord.Object(id=535598974980325386), 'Welcome <@'+str(member.id)+'> to the **Coding Helpcenter**. You are our **'+str(membercount)+''+str(numberending)+'** member! We appreciate your stay and hope that we can help you out!')
	
@client.command(pass_context=True)
async def ican(ctx, *, userrole: str):
	availableroles = ['Java', 'C/C++/C#', 'Python', 'Visual Basic .NET', 'Perl', 'Ruby', 'Swift', 'HTML', 'PHP', 'CSS', 'Javascript']
	if ctx.message.channel.id == '533784202039132170':
		if not userrole in availableroles:
			await client.say('That role doesn\'t exist or is not available for you >.< Try it again!')
		else:
			if discord.utils.get(ctx.message.server.roles, name=userrole) in ctx.message.author.roles:
				await client.say('Whoops... Looks as if ou already have that role ^0^')
			if userrole in availableroles and not discord.utils.get(ctx.message.server.roles, name=userrole) in ctx.message.author.roles:
				await client.add_roles(ctx.message.author, discord.utils.get(ctx.message.server.roles, name=userrole))
				await client.say('**'+ctx.message.author.name+'**, successfully gave you the role `'+userrole+'`!')
	else:
		return
	
@client.command(pass_context=True)
async def icant(ctx, *, todelrole: str):
	availableroles = ['Java', 'C/C++/C#', 'Python', 'Visual Basic .NET', 'Perl', 'Ruby', 'Swift', 'HTML', 'PHP', 'CSS', 'Javascript']
	if ctx.message.channel.id == '533784202039132170':
		if not todelrole in availableroles:
			await client.say('That role doesn\'t exist or is not available for you >.< Try it again!')
		else:
			if discord.utils.get(ctx.message.server.roles, name=todelrole) in ctx.message.author.roles:
				await client.remove_roles(ctx.message.author, discord.utils.get(ctx.message.server.roles, name=todelrole))
				await client.say('**'+ctx.message.author.name+'**, successfully removed the role `'+todelrole+'` from you!')
			else:
				await client.say('You don\'t even have that role >.< Can\'t remove it!')

@client.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def purge(ctx, number):
	messages = []
	async for message in client.logs_from(ctx.message.channel, limit=int(number)+1):
		messages.append(message)
	await client.delete_messages(messages)
	embed=discord.Embed(title='Messages deleted!', color=0xff0000)
	embed.add_field(name='Number of messages:', value=str(number), inline=False)
	await client.say(embed=embed)
					 
client.run(os.getenv('Token'))
