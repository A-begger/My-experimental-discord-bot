# bot.py
from email.policy import default
import os
import random
from urllib import response
import discord
from mcstatus import MinecraftServer
from discord.ext import commands
from dotenv import load_dotenv

# 1


load_dotenv()
# imports os, discord and .env
secret = os.getenv('auth')
TOKEN = secret

# fetches the token from the .env

# 2
bot = commands.Bot(command_prefix='-')
# bot prefix
@bot.event
async def on_ready():
    # this is executed when the bot is ready to run
    print(f'{bot.user.name} has connected to Discord!')
default_ip="inthessmokes.aternos.me" #Sets the default ip as a global variable

@bot.command(name='status')
# is a command, does this if status
async def server_lookup(ctx,default_ip=default_ip):
    if ctx.guild.id == 895342111933726781: #if the command is sent from a guild
        default_ip="Kaleria.aternos.me"    #with a specifc id then it changes the default ip
    server = MinecraftServer.lookup(default_ip)
    
    # 'status' is supported by all Minecraft servers that are version 1.7 or higher.
    status = server.status()
    if status.players.online == 0:
        offline = (f"The server is offline")
        response = offline
    else:
        online = (f"The server is online and has {status.players.online} player(s) online")
        response = online
    await ctx.send(response)
@bot.command(name='ping') #ping pong
async def pong(ctx):
  rand_num = random.randint(1,10)
  if rand_num == 1: 
        response = "Smoke sucks"
  else:
      response = "Pong!"
  if discord.Member.id == {317153009400414209}:
    response = "You suck"  
  await ctx.send(response)
""" If querying is enabled then this will query the server.
@bot.command(name='query')
async def info(ctx):
    server = MinecraftServer.lookup("inthessmokes.aternos.me")
    query = server.query()
    num_online=(f"The server has the following players online: {', '.join(query.players.names)}")
    response = num_online
    await ctx.send(response)
"""
bot.run(TOKEN)
# runs the bot with the token