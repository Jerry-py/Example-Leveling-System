import discord
from discord.ext import commands


class helpcommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="Help", description="Commands", color=discord.Color.red())
        embed.add_field(name="Level", value="Shows a member's rank")
        embed.add_field(name="Leaderboard", value="Shows the top 10 in the leaderboard\n Usage:\n leaderboard")
        embed.add_field(name="Set", value="Sets a user's xp or level\n Usage:\n set [level/xp] [member] [amount]")
        embed.add_field(name="Usage:", value="**rank [member]**")
        embed.add_field(name="Usage:", value="**leaderboard**")
        embed.add_field(name="Usage:", value="**set [level/xp] [member] [amount]**")
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        await ctx.send(embed=embed)
        
 

def setup(bot):
    bot.add_cog(helpcommand(bot))
