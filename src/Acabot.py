import discord
from discord.ext import commands

TOKEN = open("AcabotToken.txt", "r").read()
client = commands.Bot(command_prefix='%')

client.run(TOKEN)
