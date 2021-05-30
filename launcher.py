import discord
from discord.ext import commands, tasks
import os
from dotenv import load_dotenv
import os
from datetime import datetime
from itertools import cycle
import asyncio

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


@tasks.loop(seconds=10.0)
async def status_loop():
    statuses = cycle(["Watching members level up", 
        "Watching Jerry.py", ">help", f"Watching {len(set(bot.get_all_members()))}"
        f"users and {len(bot.guilds)} servers."])
    while True:
        await bot.change_presence(activity=discord.Game(next(statuses)))
        await asyncio.sleep(15)


@bot.event
async def on_ready():
    # Load Cogs
    load_cogs()

    # When ready
    print("READY")

    # Status
    await status_loop()



    


# Run bot
bot.run(os.getenv("TOKEN"))