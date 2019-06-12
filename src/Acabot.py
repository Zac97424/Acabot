import discord
from discord.ext import commands

TOKEN = open("AcabotToken.txt", "r").read()
client = commands.Bot(command_prefix='%')

client.load_extension('Anarpoll')
client.load_extension('Quit')
client.load_extension('Hello')

client.run(TOKEN)
