import discord
from discord.ext import commands


cmds = {
    "rank" : {
        "title": "Rank command",
        "desc": "Shows a member's rank",
        "aliases": "None",
        "usage": "```rank [member]```",
        "cooldown" : "`5`s"
    },
    "leaderboard" : {
        "title": "Leaderboard command",
        "desc": "Shows the top 10 in the leaderboard. **True** is **global** and **False** is **guild only**",
        "aliases": "None",
        "usage": "```leaderboard [true/false]```",
        "cooldown" : "`5`s"
    },
    "set" : {
        "title": "set command",
        "desc": "To set a user's xp/level",
        "aliases": "None",
        "usage" : "```set [level/xp] [member] [amount]```",
        "cooldown" : "None"
    },
    "restart" : {
        "title": "Restart command",
        "desc": "Restart the Bot",
        "aliases": "None",
        "usage" : "```restart```",
        "cooldown" : "None"
    },
    "shutdown" : {
        "title": "Shutdown command",
        "desc": "Shutdowns the bot",
        "aliases": "close",
        "usage" : "```shutdown```",
        "cooldown" : "None"
    },
    "refresh" : {
        "title": "Refresh command",
        "desc": "Refresh the current code with the code on github",
        "aliases": "pull",
        "usage" : "```refresh```",
        "cooldown" : "None"
    },
    "load" : {
        "title": "Load command",
        "desc": "Load a module",
        "aliases": "None",
        "usage" : "```load [module name]```",
        "cooldown" : "None"
    },
    "unload" : {
        "title": "Unload command",
        "desc": "Unload a module",
        "aliases": "None",
        "usage" : "```unload [cog name]```",
        "cooldown" : "None"
    },
    "reload" : {
        "title": "Reload command",
        "desc": "Reload a module",
        "aliases": "None",
        "usage" : "```reload [module name]```",
        "cooldown" : "None"
    },
    "uptime" : {
        "title": "Uptime command",
        "desc": "See Bot's Uptime",
        "aliases": "None",
        "usage" : "```uptime```",
        "cooldown" : "`5`s"
    },
    "source" : {
        "title": "Source command",
        "desc": "Get the bot source code",
        "aliases": "github/code",
        "usage" : "```uptime```",
        "cooldown" : "`5`s"
    },
    "stats" : {
        "title": "Stats command",
        "desc": "See bot's stats",
        "aliases": "statistics",
        "usage" : "```stats```",
        "cooldown" : "`5`s"
    },
    "eval" : {
        "title": "Eval command",
        "desc": "Evaluate code (command stays hidden from help command)",
        "aliases": "None",
        "usage" : "```stats```",
        "cooldown" : "None"
    },
    "image" : {
        "title": "Image command",
        "desc": "Change background for rank command",
        "aliases": "None",
        "usage" : "```image [url]```",
        "cooldown" : "`5`s"
    }
}




class helpcommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, *, command=None):
        if command is None:
            embed = discord.Embed(title="Help", description="Commands", color=discord.Color.red())
            embed.add_field(name="Level", value="Shows a member's rank")
            embed.add_field(name="Leaderboard", value="Shows the top 10 in the leaderboard. **True** is **global** and **False** is **guild only**")
            embed.add_field(name="Set", value="Sets a user's xp or level")
            embed.add_field(name="Usage:", value="```\nrank [member]```")
            embed.add_field(name="Usage:", value="```\nleaderboard [true/false]```")
            embed.add_field(name="Usage:", value="```\nset [level/xp] [member] [amount]```")
            embed.add_field(name="Image", value="Change background for rank command")
            embed.add_field(name="Restart", value="Restart the Bot")
            embed.add_field(name="Refresh", value="Refresh the current code with the code on github")
            embed.add_field(name="Usage:", value="```\nrestart```")
            embed.add_field(name="Usage:", value="```\nimage [url]```")
            embed.add_field(name="Usage:", value="```\nrefresh```")
            embed.add_field(name="Load", value="Load a module")
            embed.add_field(name="Unload", value="Unload a module")
            embed.add_field(name="Reload", value="Reload a module")
            embed.add_field(name="Usage:", value="```\nload [module name]```")
            embed.add_field(name="Usage:", value="```\nunload [module name]```")
            embed.add_field(name="Usage:", value="```\nreload [module name]```")
            embed.add_field(name="Uptime", value="See Bot's Uptime")
            embed.add_field(name="Source", value="Get the bot source code")
            embed.add_field(name="Stats", value="See bot's stats")
            embed.add_field(name="Usage:", value="```\nuptime```")
            embed.add_field(name="Usage:", value="```\nsource [command name]```")
            embed.add_field(name="Usage:", value="```\nstats```")
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            try:
                command = command.lower()
                embed = discord.Embed(title=cmds[command].get("title"))
                embed.add_field(name="Description:", value=cmds[command].get("desc"), inline=False)
                embed.add_field(name="Aliases:", value=cmds[command].get("aliases"), inline=False)
                embed.add_field(name="Cooldown:", value=cmds[command].get("cooldown"), inline=False)
                embed.add_field(name="Usage:", value=cmds[command].get("usage"), inline=False)
                embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)
            except:
                await ctx.send("Command not found")
       
        
 

def setup(bot):
    bot.add_cog(helpcommand(bot))
