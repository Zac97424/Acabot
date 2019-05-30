import discord

TOKEN = open("AcabotToken.txt", "r").read()
client = discord.Client()

client.run(TOKEN)
