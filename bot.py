# bot.py
import os
import random
from urllib import response
import discord
from mcstatus import MinecraftServer

# 1
from discord.ext import commands

from dotenv import load_dotenv

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
@bot.command(name='status')
# is a command, does this if status
async def server_lookup(ctx):
    server = MinecraftServer.lookup("inthessmokes.aternos.me")
    # 'status' is supported by all Minecraft servers that are version 1.7 or higher.
    status = server.status()
    if status.players.online == 0:
        offline = (f"The server is offline")
        response = offline
    else:
        online = (f"The server is online and has",{status.players.online},"players online")
        response = online
    await ctx.send(response)
@bot.command(name='ping') #ping pong
async def pong(ctx):
  response = "pong!"
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