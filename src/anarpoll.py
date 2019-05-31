import discord
import random
import re
from discord.ext import commands

def _anarpoll_usage(ctx):
    pass

async def _anarpoll_getEmojis(ctx, *args):
    emojis = []
    actChar = '🇦'
    for arg in args:
        emojis.append(actChar)
        actChar = chr(ord(actChar) + 1)
    return emojis

@commands.command()
async def anarpoll(ctx, question, *args):
    emojis = await _anarpoll_getEmojis(ctx, *args)
    toSend = "{0} **{1}**".format(random.choice(ctx.bot.emojis), question)
    actEmoji = 0
    for arg in args:
        toSend += '\n{0} {1}'.format(emojis[actEmoji], arg)
        actEmoji += 1
    msg = await ctx.send(toSend)
    for arg in args:
        await msg.add_reaction(emojis.pop(0))

    