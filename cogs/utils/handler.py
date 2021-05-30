import discord
from discord.ext import commands
import asyncio



class CommandErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(f"Command doesn't exist")
            return
        
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"You are cooldown. Please try again in **{error.retry_after:.2f}s**")
            return

        
        if isinstance(error, discord.ext.commands.errors.NotOwner):
            await ctx.send("You are not the owner of this bot so you can't use this command")
            return

        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have the permissions to do that! Please contact a server admin to do that for you.")
            return

        if isinstance(error, commands.ChannelNotFound):
            await ctx.send("Channel not found.")
            return
        
        
        if isinstance(error, commands.MemberNotFound):
            await ctx.send("That member doesn't exist.")
            return

        if isinstance(error, discord.Forbidden):
            await ctx.send("I can't do this. I'm forbidden to do this.")

        if isinstance(error, discord.NotFound):
            await ctx.send("Couldn't find that sorry")
            return

        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            await ctx.send("There are required arguements/parameters you need to input")
            return
        else:
            raise error


def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))