import discord
import random
import re
from discord.ext import commands

def _anarpoll_usage(ctx):
    pass

def _anarpoll_getEmojis(*args):
    emojis = [];
    actChar = 'a'
    print(len(args))
    for arg in args:
        emojis.append(":regional_indicator_{}:".format(actChar))
        actChar = chr(ord(actChar) + 1)
    return emojis

@commands.command()
async def anarpoll(ctx, question, *args):
    emojis = _anarpoll_getEmojis(*args)
    toSend = "{0} **{1}**".format(random.choice(ctx.bot.emojis), question)
    for arg in args:
        toSend += '\n{0} {1}'.format(emojis.pop(0), arg)
    await ctx.send(toSend)
    