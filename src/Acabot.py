import discord
from discord.ext import commands

from Hello import hello

TOKEN = open("AcabotToken.txt", "r").read()
client = commands.Bot(command_prefix='%')

client.load_extension('Anarpoll')
client.load_extension('Quit')

client.add_command(hello)

client.run(TOKEN)
