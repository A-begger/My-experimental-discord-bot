
# bot.py
import os
import random
import discord
from mcstatus import MinecraftServer
# 1
from discord.ext import commands
my_secret = os.environ['TOKEN']

TOKEN = my_secret
#TOKEN = os.getenv('my_secret')

# 2
bot = commands.Bot(command_prefix='s!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
@bot.command(name='status')
async def server_lookup(ctx):
    server = MinecraftServer.lookup("TheBlackHatClan.aternos.me")
    # 'status' is supported by all Minecraft servers that are version 1.7 or higher.
    status = server.status()
    if status.players.online == 0:
        offline = (f"The server is offline")
        response = offline
    else:
        online = (f"The server is online and has",{status.players.online},"players online")
        response = online
    await ctx.send(response)

bot.run(TOKEN)