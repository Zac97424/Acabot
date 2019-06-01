import discord
from discord.ext import commands

from Anarpoll import anarpoll
from Hello import hello

TOKEN = open("AcabotToken.txt", "r").read()
client = commands.Bot(command_prefix='%')

client.add_command(anarpoll)
client.add_command(hello)

client.run(TOKEN)
