import discord
from discord.ext import commands
import datetime
import time
import inspect
import os
import psutil 
import platform

obj_Disk = psutil.disk_usage('/')
start_time = time.time()



class utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def uptime(self, ctx):
        delta_uptime = datetime.datetime.utcnow() - self.bot.launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        current_time = time.time()
        difference = int(round(current_time - start_time))
        text = str(datetime.timedelta(seconds=difference))
        e = discord.Embed(title=f"Uptime,", color=discord.Color.green())
        e.add_field(name="Time:", value=f"{days}d, {hours}h, {minutes}m, {seconds}s", inline=True)
        e.add_field(name="Time Lapse:", value=text, inline=False)
        await ctx.send(embed=e)


    @commands.command(aliases=["github", "code"])
    @commands.cooldown(1, 5, commands.BucketType.channel)
    async def source(self, ctx, *, command_name=None):

        source_code = "https://github.com/Jerry-py/Example-Leveling-System"

        embed = discord.Embed(title="ConchBot Source Code")

        # If Command Parameter is None
        if command_name is None:
            embed.add_field(name="Source:", value=source_code, inline=False)
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested {ctx.author.name}#{ctx.author.discriminator}")
            await ctx.send(embed=embed)

        # Anything else
        else:
            # Get the command
            obj = self.bot.get_command(command_name.replace('.', ' '))

            # If command cannot be found
            if obj is None:
                await ctx.send('Could not find command in my github source code.')
            
            # Get the source of the code
            src = obj.callback.__code__

            # Check if its a module
            module = obj.callback.__module__

            # Get the file name
            filename = src.co_filename

            # Check if module doesn't start with discord
            if not module.startswith('discord'):
                location = os.path.relpath(filename).replace('\\', '/')
            else:
                location = module.replace('.', '/') + '.py'

            # Get the line of code for the command
            end_line, start_line = inspect.getsourcelines(src)

            # Go to the command url. Note: It is a permalink
            final_url = (f'{source_code}/blob/main/{location}#L{start_line}-L'
                     f'{start_line + len(end_line) - 1}')

            embed.add_field(name="Command Source:", value=final_url, inline=False)
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested {ctx.author.name}#{ctx.author.discriminator}")
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            await ctx.send(embed=embed)


    @commands.command(aliases=["statistics", "info", "information"])
    @commands.cooldown(1, 5, commands.BucketType.user) 
    async def stats(self, ctx):
        delta_uptime = datetime.datetime.utcnow() - self.bot.launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        current_time = time.time()
        difference = int(round(current_time - start_time))
        text = str(datetime.timedelta(seconds=difference))
        uname = platform.uname()
        embed = discord.Embed(title=f'{self.bot.user.name} Stats', colour=ctx.author.colour)
        embed.add_field(name="Bot Name:", value=self.bot.user.name)
        embed.add_field(name="Bot Id:", value=self.bot.user.id)
        embed.add_field(name="Bot Version:", value="1.0.1")
        embed.add_field(name="Python Version:", value=platform.python_version())
        embed.add_field(name="Discord.py Version:", value=discord.__version__)
        embed.add_field(name="Total Guilds:", value=len(self.bot.guilds))
        embed.add_field(name="Total Users:", value=len(set(self.bot.get_all_members())))
        embed.add_field(name="Total Commands:", value=len(set(self.bot.commands)))
        embed.add_field(name="Total Cogs:", value=len(set(self.bot.cogs)))
        embed.add_field(name="System:", value=uname.system)
        embed.add_field(name="System Version", value=uname.version)
        embed.add_field(name="Machine:", value=uname.machine)
        embed.add_field(name="Processor:", value=uname.processor)
        embed.add_field(name="Total CPU Usage:", value=psutil.cpu_percent())
        embed.add_field(name="Total RAM:", value=psutil.virtual_memory()[2])
        embed.add_field(name="Total Space:", value=obj_Disk.total / (1024.0 ** 3))
        embed.add_field(name="Total Spaced Used:", value=obj_Disk.used / (1024.0 ** 3))
        embed.add_field(name="Total Space Left:", value=obj_Disk.free / (1024.0 ** 3))
        embed.add_field(name="Uptime:", value=f"{days}d, {hours}h, {minutes}m, {seconds}s", inline=True)
        embed.add_field(name="Uptime Lapse:", value=text)
        embed.add_field(name="Bot Developers:", value="Jerry.py#7611")
        embed.add_field(name="Bot Developers Ids:", value="Jerry.py - 789535039406473276")
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested {ctx.author.name}#{ctx.author.discriminator}")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(utils(bot))