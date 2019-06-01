import discord
import random
import re
from discord.ext import commands

async def _anarpoll_getEmojis(*args):
	emojis = []
	actChar = '🇦'
	for arg in args:
		emojis.append(actChar)
		actChar = chr(ord(actChar) + 1)
	return emojis

async def _anarpoll_impl(ctx, question, *args):
	if (len(args) > 20):
		await ctx.send("Désolé {}, je ne peux pas mettre plus de 20 propositions. :cry:".format(ctx.author.mention))
		return
	emojis = await _anarpoll_getEmojis(*args)
	toSend = "{0} **{1}**".format(random.choice(ctx.bot.emojis), question)
	actEmoji = 0
	for arg in args:
		toSend += '\n{0} {1}'.format(emojis[actEmoji], arg)
		actEmoji += 1
	msg = await ctx.send(toSend)
	for arg in args:
		await msg.add_reaction(emojis.pop(0))

class Anarpoll(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def anarpoll(self, ctx, question, *args):
		await _anarpoll_impl(ctx, question, *args)

	@commands.command()
	async def anarpolls(self, ctx, question, minutes, *args):
		await _anarpoll_impl(ctx, question, *args)

	@commands.command()
	async def anarpollm(self, ctx, question, minutes, *args):
		await _anarpoll_impl(ctx, question, *args)

	@commands.command()
	async def anarpollh(self, ctx, question, hours, *args):
		await _anarpoll_impl(ctx, question, *args)

def setup(bot):
	bot.add_cog(Anarpoll(bot))