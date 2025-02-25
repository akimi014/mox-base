from discord.ext import commands

class Fala(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def falar(self, ctx:commands.Context, *, fala):
		await ctx.send(rf'{fala}')

async def setup(bot):
	await bot.add_cog(Fala(bot))