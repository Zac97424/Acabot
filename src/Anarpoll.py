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
		toSend += "\n{0} {1}".format(emojis[actEmoji], arg)
		actEmoji += 1
	msg = await ctx.send(toSend)
	for arg in args:
		await msg.add_reaction(emojis.pop(0))
	return msg

class _AnarpollContainer:
	def __init__(self, message, question, *propositions):
		self.Message = message
		self.Question = question
		self.Propositions = [*propositions]

def _anarpoll_findpoll(polls, question):
	poll = None
	hasFound = False
	for Poll in polls:
		if Poll.Question == question:
			poll = Poll
			hasFound = True
			break
	return poll, hasFound

class Anarpoll(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.Polls = []

	@commands.command()
	async def anarpoll(self, ctx, question, *args):
		message = await _anarpoll_impl(ctx, question, *args)
		self.Polls.append(_AnarpollContainer(message, question, *args))

	@commands.command()
	async def anarpolls(self, ctx, question, seconds, *args):
		message = await _anarpoll_impl(ctx, question, *args)
		self.Polls.append(_AnarpollContainer(message, question, *args))

	@commands.command()
	async def anarpollm(self, ctx, question, minutes, *args):
		message = await _anarpoll_impl(ctx, question, *args)
		self.Polls.append(_AnarpollContainer(message, question, *args))

	@commands.command()
	async def anarpollh(self, ctx, question, hours, *args):
		message = await _anarpoll_impl(ctx, question, *args)
		self.Polls.append(_AnarpollContainer(message, question, *args))

	@commands.command()
	async def anarpoll_delete(self, ctx, question):
		poll, hasFound = _anarpoll_findpoll(self.Polls, question)
		if not hasFound:
			await ctx.send("Wesh t'as cru je pouvais supprimer un poll qu'existe pas ? :thinking:")
			return
		self.Polls.remove(poll)
		await ctx.send("C'est bon ! Le poll est supprimé ! :grin:")

	@commands.command()
	async def anarpoll_add(self, ctx, question, arg):
		poll, hasFound = _anarpoll_findpoll(self.Polls, question)
		if not hasFound:
			await ctx.send("Désolé·e, je n'ai pas trouvé le poll demandé :cry:")
			return
		poll.Propositions.append(arg)
		msg = await _anarpoll_impl(ctx, question, *poll.Propositions)
		poll.Message = msg

	@commands.command()
	async def anarpoll_remove(self, ctx, question, arg):
		poll, hasFound = _anarpoll_findpoll(self.Polls, question)
		if not hasFound:
			await ctx.send("Ton poll existe pas, déso pas déso :shrug:")
			return
		if poll.Propositions.count(arg) == 0:
			await ctx.send("Excuses moi, mais ta proposition n'existe pas pour ce poll :neutral_face:")
			return
		poll.Propositions.remove(arg)
		msg = await _anarpoll_impl(ctx, question, *poll.Propositions)
		poll.Message = msg

def setup(bot):
	bot.add_cog(Anarpoll(bot))