import discord
from discord.ext import commands

@commands.command()
async def hello(ctx):
    await ctx.send("Coucou {} :wave:".format(ctx.author.mention))