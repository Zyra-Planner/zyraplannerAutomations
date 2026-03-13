import discord
from discord.ext import commands
import os
import asyncio

TOKEN = os.getenv("DISCORD_TOKEN")

class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(
            command_prefix="!",
            intents=intents
        )

    async def setup_hook(self):
        # load commands
        for file in os.listdir("./bot/commands"):
            if file.endswith(".py"):
                await self.load_extension(f"bot.commands.{file[:-3]}")

async def main():
    bot = Bot()
    async with bot:
        await bot.start(TOKEN)

asyncio.run(main())
