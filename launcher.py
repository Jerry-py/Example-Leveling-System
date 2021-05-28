import discord
from discord.ext import commands
import os
import jishaku
from dotenv import load_dotenv
import os

env = load_dotenv()

# MAKE SURE TO HAVE INTENTS ON
bot = commands.Bot(command_prefix=">", intents=discord.Intents.all())

# Load cogs
print("Loading All cogs...")
print("------")
for filename in os.listdir(f"./cogs"):
    if filename.endswith(f".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")
        print(f"Loaded `{filename[:20]}` Cog")

print("------")
bot.load_extension('cogs.utils.handler')
print("Loaded `Error Handler` Cog")
print("------")
bot.load_extension('jishaku')
print("Loaded `jishaku`")
print("------")


@bot.event
async def on_ready():
    # When ready
    print("READY")

# Run bot
bot.run(os.getenv("TOKEN"))