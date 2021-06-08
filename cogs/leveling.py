import discord
from discord.ext import commands
import sqlite3
import vacefron
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import aiohttp
import io
import math



vac_api = vacefron.Client()



class levelingsys(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Credits to Coding Adda -> https://github.com/Wiper-R/Basic-Bot/blob/ea961dc6f793c5d019103b6a4b68c2e79aa96dda/cogs/levelling.py#L187#L61

    async def make_rank_image(self, member: discord.Member, rank, level, xp, level_up_xp, background):
        user_avatar_image = str(member.avatar_url_as(format='png', size=512))
        async with aiohttp.ClientSession() as session:
            async with session.get(user_avatar_image) as resp:
                avatar_bytes = io.BytesIO(await resp.read())

        async with aiohttp.ClientSession() as session:
            async with session.get(background) as resp:
                background_bytes = io.BytesIO(await resp.read())

        # Background
        background = Image.open(background_bytes).resize(((1000, 240)))

        # User avatar
        logo = Image.open(avatar_bytes).resize((200, 200))

        # Avatar
        bigsize = (logo.size[0] * 3, logo.size[1] * 3)
        mask = Image.new('L', bigsize, 0)
        draw = ImageDraw.Draw(mask) 
        draw.ellipse((0, 0) + bigsize, fill=255)
        mask = mask.resize(logo.size, Image.ANTIALIAS)
        logo.putalpha(mask)
        background.paste(logo, (20, 20), mask=logo)
        draw = ImageDraw.Draw(background, 'RGB')
        draw.ellipse((152, 152, 208, 208), fill='#000')
        draw.ellipse((155, 155, 205, 205), fill='#43B581')

        # Fonts
        big_font = ImageFont.FreeTypeFont('./storage/fonts/ABeeZee-Regular.otf', 60)
        medium_font = ImageFont.FreeTypeFont('./storage/fonts/ABeeZee-Regular.otf', 40)
        small_font = ImageFont.FreeTypeFont('./storage/fonts/ABeeZee-Regular.otf', 30)
        bigger_small_font = ImageFont.FreeTypeFont('./storage/fonts/ABeeZee-Regular.otf', 35)
        smaller_font = ImageFont.FreeTypeFont('./storage/fonts/ABeeZee-Regular.otf', 15)
        other_font =  ImageFont.FreeTypeFont('./storage/fonts/SourceSansPro-Black.otf', 40)

        # Drawing on the background image
        draw1 = ImageDraw.Draw(background) 

        text_size = draw.textsize(f"{level}", font=big_font)
        offset_x = 1000-15 - text_size[0]
        offset_y = 5 
        draw.text((offset_x, offset_y), f"{level}", font=big_font, fill="#11ebf2")
        text_size = draw.textsize('Level:', font=small_font)

        offset_x -= 5 + text_size[0]
        offset_y = 35
        draw.text((offset_x, offset_y), "Level:", font=small_font, fill="#11ebf2")

        # Placing Rank Text (right upper part)
        text_size = draw.textsize(f"#{rank}", font=big_font)
        offset_x -= 15 + text_size[0]
        offset_y = 8
        draw.text((offset_x, offset_y), f"#{rank}", font=big_font, fill="#fff")

        text_size = draw.textsize("Rank:", font=small_font)
        offset_x -= 5 + text_size[0]
        offset_y = 35
        draw.text((offset_x, offset_y), "Rank:", font=small_font, fill="#fff")

        # Progress Bar
        bar_offset_x = logo.size[0] + 20 + 40
        bar_offset_y = 160
        bar_offset_x_1 = 1000 - 50
        bar_offset_y_1 = 200
        circle_size = bar_offset_y_1 - bar_offset_y
        draw1.rectangle((bar_offset_x, bar_offset_y, bar_offset_x_1, bar_offset_y_1), fill="#727175")
        draw1.ellipse((bar_offset_x - circle_size//2, bar_offset_y, bar_offset_x + circle_size//2, bar_offset_y + circle_size), fill="#727175")
        draw1.ellipse((bar_offset_x_1 - circle_size//2, bar_offset_y, bar_offset_x_1 + circle_size//2, bar_offset_y_1), fill="#727175")
        bar_length = bar_offset_x_1 - bar_offset_x
        progress = (level_up_xp - xp) * 100/level_up_xp
        progress = 100 - progress
        progress_bar_length = round(bar_length * progress/100)
        pbar_offset_x_1 = bar_offset_x + progress_bar_length
        draw1.rectangle((bar_offset_x, bar_offset_y, pbar_offset_x_1, bar_offset_y_1), fill="#11ebf2")
        draw1.ellipse((bar_offset_x - circle_size//2, bar_offset_y, bar_offset_x + circle_size//2, bar_offset_y + circle_size), fill="#11ebf2")
        draw1.ellipse((pbar_offset_x_1 - circle_size//2, bar_offset_y, pbar_offset_x_1 + circle_size//2, bar_offset_y_1), fill="#11ebf2")


        # Member Name Text
        member_name_text = f"{member.display_name}"
        text_size = draw1.textsize(member_name_text, font=big_font)
        text_offset_x = bar_offset_x - 20
        text_offset_y = bar_offset_y - text_size[1] - 80
        draw1.text((text_offset_x, text_offset_y), member_name_text, font=big_font, fill="#fff")

        # Member Discriminator Text
        member_discriminator_text = f"#{member.discriminator}"
        text_offset_x += text_size[0] + 10
        text_size = draw1.textsize(member_discriminator_text, font=medium_font)
        text_offset_y = bar_offset_y - text_size[1] - 90
        draw1.text((text_offset_x, text_offset_y), member_discriminator_text, font=medium_font, fill="#727175")
        

        # Level Text
        level_text = f"Level: {level}"
        

        # XP Text
        xp_text = f"XP: {xp}/{level_up_xp}"
        xp_text_size = draw1.textsize(xp_text, font=bigger_small_font)
        xp_offset_x = bar_offset_x_1 - xp_text_size[0]
        xp_offset_y = bar_offset_y - xp_text_size[1] - 10
        draw1.text((xp_offset_x, xp_offset_y), xp_text, font=bigger_small_font, fill="#727175")


        # Percentage Text
        percentage_text = f"{int(100/level_up_xp * xp)}%"
        text_size = draw.textsize(percentage_text, font=other_font)
        text_offset_x = bar_offset_x - 10
        text_offset_y = bar_offset_y - text_size[1] - 5
        draw1.text((text_offset_x, text_offset_y), percentage_text, font=other_font, fill="#fff")

        # Rank Text
        rank_text = f"#{rank}/{member.guild.id}"

        

        bytes = io.BytesIO()
        background.save(bytes, 'JPEG')
        bytes.seek(0)
        return bytes




    @commands.group(invoke_without_command=True)
    @commands.is_owner()
    async def set(self, ctx):
        # Set commands
        await ctx.send("USE `set xp` or `set level`")

    # Set xp for a user
    @set.command()
    @commands.is_owner()
    async def xp(self, ctx, member: discord.Member=None, *, amount=None):
        if member is None:
            await ctx.send("You need to mention them")
        if amount is None:
            await ctx.send("You need to put a amount")
        db = sqlite3.connect("./db/leveling.db")
        cursor = db.cursor()
        cursor.execute(f"SELECT userid FROM users WHERE guildid = '{ctx.guild.id}'")
        result = cursor.fetchone()
        if result is None:
            sql = ("INSERT INTO users(guildid, userid, level, xp, level_up_xp, rank_image_url) VALUES(?, ?, ?, ?, ?, ?)")
            val = (str(ctx.guild.id), str(ctx.author.id), 1, amount, 100, "https://media.discordapp.net/attachments/818899477372600434/848947456334495794/Leveling_System_Background_3.jpg")
            cursor.execute(sql, val)
            db.commit()
        sql = ("UPDATE users SET xp = ? WHERE guildid = ? and userid = ?")
        val = (amount, str(ctx.guild.id), str(member.id))
        cursor.execute(sql, val)
        db.commit()
        await ctx.send("Done")

    # Set level for a user
    @set.command()
    @commands.is_owner()
    async def level(self, ctx, member: discord.Member=None, *, amount=None):
        if member is None:
            await ctx.send("You need to mention them")
        if amount is None:
            await ctx.send("You need to put a amount")
        db = sqlite3.connect("./db/leveling.db")
        cursor = db.cursor()
        cursor.execute(f"SELECT userid FROM users WHERE guildid = '{ctx.guild.id}'")
        result = cursor.fetchone()
        if result is None:
            sql = ("INSERT INTO users(guildid, userid, level, xp, level_up_xp, rank_image_url) VALUES(?, ?, ?, ?, ?, ?)")
            val = (str(ctx.guild.id), str(ctx.author.id), amount, 10, 100, "https://media.discordapp.net/attachments/818899477372600434/848947456334495794/Leveling_System_Background_3.jpg")
            cursor.execute(sql, val)
            db.commit()
            return
        sql = ("UPDATE users SET level = ? WHERE guildid = ? and userid = ?")
        val = (amount, str(ctx.guild.id), str(member.id))
        cursor.execute(sql, val)
        db.commit()
        await ctx.send("Done")
    

    @commands.Cog.listener()
    async def on_member_join(self, member):
        db = sqlite3.connect("./db/leveling.db")
        cursor = db.cursor()
        sql = ("INSERT INTO users(guildid, userid, level, xp, level_up_xp, rank_image_url) VALUES(?, ?, ?, ?, ?, ?)")
        val = (str(member.guild.id), str(member.id), 1, 0, 100, "https://media.discordapp.net/attachments/818899477372600434/848947456334495794/Leveling_System_Background_3.jpg")
        cursor.execute(sql, val)
        db.commit()


    @commands.Cog.listener()
    async def on_member_leave(self, member):
        db = sqlite3.connect("./db/leveling.db")
        cursor = db.cursor()
        cursor.execute(f"DELETE FROM users WHERE userid = {member.id}")
        db.commit()



    @commands.Cog.listener()
    async def on_message(self, message):
        # If bot is sending the message
        if message.author.bot:
            return
        
        # DB info
        db = sqlite3.connect("./db/leveling.db")
        cursor = db.cursor()

        # Getting info from the user
        cursor.execute(f"SELECT userid FROM users WHERE guildid = '{message.guild.id}'")

        # Fetch one result
        result = cursor.fetchone()

        # If the db can't find anything
        if result is None:
            # Insert the user
            sql = ("INSERT INTO users(guildid, userid, level, xp, level_up_xp, rank_image_url) VALUES(?, ?, ?, ?, ?, ?)")
            val = (str(message.guild.id), str(message.author.id), 1, 10, 100, "https://media.discordapp.net/attachments/818899477372600434/848947456334495794/Leveling_System_Background_3.jpg")
            cursor.execute(sql, val)

            # Commit to the db
            db.commit()

        # If the db found something
        else:
            # Getting the user info again
            cursor.execute(f"SELECT userid, xp, level, level_up_xp FROM users WHERE guildid = '{message.guild.id}' and userid = '{message.author.id}'")

            # Fetch the user info once
            result1 = cursor.fetchone()
            # xp variable
            exp = int(result1[1])

            # Updating db
            sql = ("UPDATE users SET xp = ? WHERE guildid = ? and userid = ?")
            val = (int(exp) + 10, str(message.guild.id), str(message.author.id))
            cursor.execute(sql, val)

            # Commit to db
            db.commit()

            # More info
            xp = int(result1[1])
            exp_until_lvl_up = int(result1[3])
            lvl = int(result1[2])
            lvl_up = lvl + int(1)
            next_exp_until_lvl_up = exp_until_lvl_up + int(100)

            # If the user reaches the amount to level up
            if xp == exp_until_lvl_up or xp > exp_until_lvl_up:
                # Send the message to notify the user
                await message.channel.send(f"GG {message.author.mention} level up to {lvl_up}")

                # Updating db
                sql = ("UPDATE users SET xp = ?, level = ?, level_up_xp = ? WHERE guildid = ? and userid = ?")
                val = (0, int(lvl_up), int(next_exp_until_lvl_up),str(message.guild.id), str(message.author.id))
                cursor.execute(sql, val)
                db.commit()


    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def rank(self, ctx, member: discord.Member=None):
        if member is None:
            member = ctx.author

        # DB info
        db = sqlite3.connect("./db/leveling.db")
        cursor = db.cursor()

        # Get everything except guildid
        cursor.execute(f"SELECT userid, level, xp, level_up_xp, rank_image_url FROM users WHERE guildid = '{ctx.guild.id}' AND userid = '{member.id}'")

        # Get a/one result
        result = cursor.fetchone()

        # If then user is not in db
        if result is None:
            sql = ("INSERT INTO users(guildid, userid, level, xp, level_up_xp, rank_image_url) VALUES(?, ?, ?, ?, ?, ?)")
            val = (str(ctx.guild.id), str(member.id), 1, 10, 100, "https://media.discordapp.net/attachments/818899477372600434/848947456334495794/Leveling_System_Background_3.jpg")
            cursor.execute(sql, val)
            db.commit()
            return

        # If they are in db
        # Info
        xp = str(result[2])
        level_up_xp = result[3]

        # Rank in leaderboard
        rank = 1

        # Find what rank the user is at
        for value in cursor:
            if xp < value[0]:
                rank += 1

        # More info
        exp = int(result[2])
        level = int(result[1])
        lvl_up_xp = int(result[3])

        rank_card = await self.make_rank_image(member, rank, level, exp, lvl_up_xp, result[4])
        file = discord.File(rank_card, f"{member.display_name}_rank_card.png")
        await ctx.send(file=file)
            
        


        



    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def leaderboard(self, ctx, *, all_time=None):
        if all_time is None:
            # DB info
            db = sqlite3.connect('db/leveling.db')
            cursor = db.cursor()

            # Ordering - Limit is 10
            cursor.execute(f"SELECT userid, level, xp from users WHERE guildid = '{ctx.guild.id}' ORDER BY level + 0 DESC, xp + 0 DESC LIMIT 10")

            # Fectch all result
            end = cursor.fetchall()

            # Embed
            embed = discord.Embed(title=f"{ctx.guild.name}'s Leaderboard: Top 10", description=f"All time in this guild: {ctx.guild.name}", color=discord.Color.green())
            for i, x in enumerate(end, 1): # End is the ending number and 1 is the start number. This is a loop
                embed.add_field(name=f"#{i}", value=f"Name: <@{x[0]}>\n Level: {x[1]}\n XP: {x[2]}", inline=False) # I is number so like #1 and the others are labled

            # Sending the embed
            await ctx.send(embed=embed)
            return
        if all_time == "True" or 'true':
            # DB info
            db = sqlite3.connect('db/leveling.db')
            cursor = db.cursor()

            # Ordering - Limit is 10
            cursor.execute(f"SELECT userid, level, xp from users ORDER BY level + 0 DESC, xp + 0 DESC LIMIT 10")

            # Fectch all result
            end = cursor.fetchall()

            # Embed
            embed = discord.Embed(title=f"All Time Leaderboard: Top 10", description="All time in every guild", color=discord.Color.green())
            for i, x in enumerate(end, 1): # End is the ending number and 1 is the start number. This is a loop
                embed.add_field(name=f"#{i}", value=f"Name: <@{x[0]}>\n Level: {x[1]}\n XP: {x[2]}", inline=False) # I is number so like #1 and the others are labled

            # Sending the embed
            await ctx.send(embed=embed)
            return

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def image(self, ctx, url):
        # DB info
        db = sqlite3.connect('db/leveling.db')
        cursor = db.cursor()

        cursor.execute(f"SELECT rank_image_url FROM users WHERE guildid = '{ctx.guild.id}' AND userid = '{ctx.author.id}'")
        result = cursor.fetchone()
        if result is None:
            sql = ("INSERT INTO users(guildid, userid, level, xp, level_up_xp, rank_image_url) VALUES(?, ?, ?, ?, ?, ?)")
            val = (str(ctx.guild.id), str(ctx.author.id), 1, 10, 100, "https://media.discordapp.net/attachments/818899477372600434/848947456334495794/Leveling_System_Background_3.jpg")
            cursor.execute(sql, val)
            db.commit()
        sql = ("UPDATE users SET rank_image_url = ? WHERE guildid = ? and userid = ?")
        val = (str(url), str(ctx.guild.id), str(ctx.author.id))
        cursor.execute(sql, val)
        db.commit()
        await ctx.send(f"Image has been set to {url}")
    

def setup(bot):
    bot.add_cog(levelingsys(bot))

