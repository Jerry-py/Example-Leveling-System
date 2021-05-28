import discord
from discord.ext import commands
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

def setup(bot):
    bot.add_cog(owner(bot))