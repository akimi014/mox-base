import discord
from discord.ext import commands

class Atividade(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		await self.bot.change_presence(
			status=discord.Status.idle,
			activity=discord.Game(name='In development.')
		)

async def setup(bot):
	await bot.add_cog(Atividade(bot))