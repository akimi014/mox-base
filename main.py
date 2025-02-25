#Main archive
import discord, os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

class Mox(commands.Bot):
	def __init__(self):
		intents =  discord.Intents.all()
		super().__init__(command_prefix='.', intents=intents, help_command=None)

	async def load_cogs(self):
		for dirpath, _, filenames in os.walk('/home/Moxyz/cogs'):
			for filename in filenames:
				if filename.endswith('.py'):
					relative = os.path.relpath(dirpath, '/home/Moxyz/cogs')
					if relative == '.':
						module = f'cogs.{filename[:-3]}'
					else:
						module = f'cogs.{relative.replace(os.sep, '.')}.{filename[:-3]}'
					try:
						await self.load_extension(module)
					except Exception as e:
						print(f'Falhou no carregamento {module}: {e}')

	async def setup_hook(self):
		await self.load_cogs()
		await self.tree.sync()
		print('Carregado.')

if __name__ == "__main__":
	mox = Mox()

	mox.run(str(os.getenv('DISCORD_TOKEN')))
