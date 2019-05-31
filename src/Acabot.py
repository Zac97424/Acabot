import discord
from discord.ext import commands

from Anarpoll import anarpoll

TOKEN = open("AcabotToken.txt", "r").read()
client = commands.Bot(command_prefix='%')

client.add_command(anarpoll)

client.run(TOKEN)
