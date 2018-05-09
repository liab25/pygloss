import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

description = 'A bot that defines basic Python terminology'
bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command
async def whatis(*args):
    if args == 'for':
        



bot.run('NDQzNDIzNDY4NjI1NzIzNDEy.DdTl4Q.siQow6uu8jHZRkXdPoFOntjWF6o')
