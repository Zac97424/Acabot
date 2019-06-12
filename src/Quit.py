import discord
from discord.ext import commands

class Quit(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def quit(self, ctx):
		await ctx.bot.logout()

def setup(bot):
	bot.add_cog(Quit(bot))