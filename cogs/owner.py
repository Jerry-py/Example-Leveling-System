import discord
from discord.ext import commands
from discord.ext.commands.core import command
from discord.ext.commands.errors import MissingPermissions
from jishaku.codeblocks import codeblock_converter
import asyncio
import os
import sys

class owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=["close"])
    async def shutdown(self, ctx):
        await ctx.send("Ending Python process ConchBot... Goodbye")
        await self.bot.logout()

    @commands.command(aliases=["pull"])
    @commands.is_owner()
    async def refresh(self, ctx):
        cog = self.client.get_cog("Jishaku")
        await cog.jsk_git(ctx, argument=codeblock_converter(f'stash'))
        await asyncio.sleep(2)
        await cog.jsk_git(ctx, argument=codeblock_converter(f'pull --ff-only https://github.com/Jerry-py/Example-Leveling-System main'))
        await asyncio.sleep(2)
        restart = self.client.get_command('restart')
        await ctx.invoke(restart)


    @commands.command()
    @commands.is_owner()
    async def restart(self, ctx):
        def restarter():
            python = sys.executable
            os.execl(python, python, * sys.argv)

        embed = discord.Embed(title="Bot Restarting...")
        embed.add_field(name="I'll be back soon...", value="Don't worry", inline=True)
        await ctx.send(embed=embed)
        restarter()

    @commands.command()
    async def reload(self, ctx, *, module):
        try:
            if os.path.exists("custom_cogs/{}.py".format(module)):
                self.bot.reload_extension("custom_cogs.{}".format(module))
            elif os.path.exists("cogs/{}.py".format(module)):
                self.bot.reload_extension("cogs.{}".format(module))
            else:
                raise ImportError("No module named '{}'".format(module))
        except Exception as e:
            await ctx.send('Failed to reload module: `{}.py`'.format(module))
            await ctx.send('{}: {}'.format(type(e).__name__, e))
        else:
            await ctx.send('Reloaded module: `{}.py`'.format(module))
        print("------")
        print(f"Reloaded `{module}` Cog")

    @commands.command()
    async def unload(self, ctx, *, module):
        try:
            if os.path.exists("cogs/{}.py".format(module)):
                self.bot.unload_extension("cogs.{}".format(module))
            elif os.path.exists("custom_cogs/{}.py".format(module)):
                self.bot.unload_extension("custom_cogs.{}".format(module))
            else:
                raise ImportError("No module named '{}'".format(module))
        except Exception as e:
            await ctx.send('Failed to unload module: `{}.py`'.format(module))
            await ctx.send('{}: {}'.format(type(e).__name__, e))
        else:
            await ctx.send('Unloaded module: `{}.py`'.format(module))
        print("------")
        print(f"Unloaded `{module}` Cog")

    @commands.command()
    async def load(self, ctx, *, module):
        try:
            if os.path.exists("cogs/{}.py".format(module)):
                self.bot.load_extension("cogs.{}".format(module))
            elif os.path.exists("custom_cogs/{}.py".format(module)):
                self.bot.load_extension("custom_cogs.{}".format(module))
            else:
                raise ImportError("No module named '{}'".format(module))
        except Exception as e:
            await ctx.send('Failed to load module: `{}.py`'.format(module))
            await ctx.send('{}: {}'.format(type(e).__name__, e))
        else:
            await ctx.send('Loaded module: `{}.py`'.format(module))
        print("------")
        print(f"Loaded `{module}` Cog")

    @commands.command()
    @commands.is_owner()
    async def eval(self, ctx, *, code: codeblock_converter):
        cog = self.bot.get_cog("Jishaku")
        await cog.jsk_python(ctx, argument=code)

def setup(bot):
    bot.add_cog(owner(bot))