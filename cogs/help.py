import discord
from discord.ext import commands


class helpcommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        embed = discord.Embed(title="Help")
        embed.add_field(name="Rank", value="Shows a member's rank")
        embed.add_field(name="Leaderboard", value="Shows the top 10 in the leaderboard")
        embed.add_field(name="Set", value="Sets a user's xp or level")
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        await ctx.send(embed=embed)
        
    @help.command()
    async def set(self, ctx):
        embed = discord.Embed(title="Set", description="Command to set the user's xp/level")
        embed.add_field(name="Usage", value="set [xp/level] [member] [amount]")
        await ctx.send(embed=embed)


    @help.command()
    async def rank(self, ctx):
        embed = discord.Embed(title="Rank", description="Command to set the user's Stats")
        embed.add_field(name="Usage", value="rank [member]")
        await ctx.send(embed=embed)

    @help.command()
    async def leaderboard(self, ctx):
        embed = discord.Embed(title="Set", description="Command to set the user's xp/level")
        embed.add_field(name="Usage", value="leaderboard")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(helpcommand(bot))


