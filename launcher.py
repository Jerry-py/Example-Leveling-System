import discord
from discord.ext import commands
import os
import jishaku
from dotenv import load_dotenv
import os
import time
from datetime import datetime

env = load_dotenv()

# MAKE SURE TO HAVE INTENTS ON
bot = commands.Bot(command_prefix=commands.when_mentioned_or(">"), intents=discord.Intents.all())
bot.launch_time = datetime.utcnow()


# So we can have our custom Help cmd
bot.remove_command('help')



# Load cogs
def load_cogs():
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
    # Load Cogs
    load_cogs()

    # When ready
    print("READY")


# Run bot
bot.run(os.getenv("TOKEN"))