import discord
from discord.ext import commands


class helpcommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="Help", description="Commands", color=discord.Color.red())
        embed.add_field(name="Level", value="Shows a member's rank")
        embed.add_field(name="Leaderboard", value="Shows the top 10 in the leaderboard")
        embed.add_field(name="Set", value="Sets a user's xp or level")
        embed.add_field(name="Usage:", value="**rank [member]**")
        embed.add_field(name="Usage:", value="**leaderboard**")
        embed.add_field(name="Usage:", value="**set [level/xp] [member] [amount]**")
        embed.add_field(name="Restart", value="Restart Bot")
        embed.add_field(name="Shutdown", value="Shutdowns the bot")
        embed.add_field(name="Refresh", value="Refresh the current code with the code on github")
        embed.add_field(name="Usage:", value="**restart**")
        embed.add_field(name="Usage:", value="**shutdown**")
        embed.add_field(name="Usage:", value="**refresh**")
        embed.add_field(name="Load", value="Load a module")
        embed.add_field(name="Unload", value="Unload a module")
        embed.add_field(name="Reload", value="Reload a module")
        embed.add_field(name="Usage:", value="**load [module name]**")
        embed.add_field(name="Usage:", value="**unload [module name]**")
        embed.add_field(name="Usage:", value="**reload [module name]**")
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
        
 

def setup(bot):
    bot.add_cog(helpcommand(bot))
