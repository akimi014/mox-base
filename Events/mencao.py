import discord
from discord.ext import commands

class Mencao(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_message(self, message):
		if self.bot.user in message.mentions:
			await message.reply('Olá!')

async def setup(bot):
	await bot.add_cog(Mencao(bot))