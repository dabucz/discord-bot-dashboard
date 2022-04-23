import discord
from discord.ext import commands
import random
import os, string
from dotenv import load_dotenv
import asyncio
load_dotenv()
import time
FOOTER = os.getenv('FOOTER')
ICON = os.getenv('ICON_URL')
pepe = ["nemáš ho", "8==D", "8===D", "8=====D", "8======D", "8===============D"]

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['s'])
    async def say(self,ctx, *, question):
      await ctx.message.delete()
      embed = discord.Embed(title=f"{question}",colour=0x00FF00)
      embed.set_footer(text=FOOTER, icon_url=ICON)
      await ctx.send(embed=embed)

    @commands.command()
    async def howgay(self,ctx, member: discord.Member=None):
      if not member:
        member = ctx.author
      embed = discord.Embed(title="gay machine",description=member.mention + " is " +str(random.randint(0, 100)) + "% gay :rainbow_flag:",color=0x00ff00)
      embed.set_footer(text=FOOTER, icon_url=ICON)
      await ctx.send(embed=embed)

    @commands.command()
    async def pp(self,ctx, member: discord.Member=None):
      if not member:
        member = ctx.author
      embed = discord.Embed(title="peepee machine",description=member.mention + " have " + random.choice(pepe),color=0x00ff00)
      embed.set_footer(text=FOOTER, icon_url=ICON)
      await ctx.send(embed=embed)


    @commands.command()
    async def hack(self,ctx,member: discord.Member=None):
        if not member:
            member = ctx.author
        email = ["@gmail.com", "@seznam.cz", "@zoznam.sk"]

        msg = await ctx.send(f"Hacking {member.name}...")
        time.sleep(2)
        await msg.edit(content=f"[▗] Bypassing discord login...")
        time.sleep(2)
        await msg.edit(content=f"[▖] Found:\nEmail: " + ("").join(random.choices(string.ascii_letters, k=10)) + ("").join(random.choices(email)) + "\nDiscord pass: " + ("").join(random.choices(string.ascii_letters, k=6)) + "\nEmail pass: " + ("").join(random.choices(string.ascii_letters, k=6)))
        time.sleep(2)
        await msg.edit(content=f"[▘] Ip logging...")
        time.sleep(2)       
        await msg.edit(content=f"[▝] Found:\nIP: " + ("").join(random.choices(string.digits, k=3)) + "." + ("").join(random.choices(string.digits, k=3)) + "." + ("").join(random.choices(string.digits, k=3)) + ":" + ("").join(random.choices(string.digits, k=5)) + "\nToken: " + ("").join(random.choices(string.ascii_letters + string.digits, k=16)))
        time.sleep(2)       
        await msg.edit(content=f"Finished hacking {member.name}")
    
    @commands.command()
    async def hack2(self,ctx,member: discord.Member=None):
        if not member:
            member = ctx.author
        email = ["@gmail.com", "@seznam.cz", "@zoznam.sk"]

        msg = await ctx.send(f"Hacking {member.name}...")
        time.sleep(2)
        await ctx.send(f"[▗] Bypassing discord login...")
        time.sleep(2)
        await ctx.send(f"[▖] Found:\nEmail: " + ("").join(random.choices(string.ascii_letters, k=10)) + ("").join(random.choices(email)) + "\nDiscord pass: " + ("").join(random.choices(string.ascii_letters, k=6)) + "\nEmail pass: " + ("").join(random.choices(string.ascii_letters, k=6)))
        time.sleep(2)
        await ctx.send(f"[▘] Ip logging...")
        time.sleep(2)       
        await ctx.send(f"[▝] Found:\nIP: " + ("").join(random.choices(string.digits, k=3)) + "." + ("").join(random.choices(string.digits, k=3)) + "." + ("").join(random.choices(string.digits, k=3)) + ":" + ("").join(random.choices(string.digits, k=5)) + "\nToken: " + ("").join(random.choices(string.ascii_letters + string.digits, k=16)))
        time.sleep(2)       
        await ctx.send(f"Finished hacking {member.name}")

def setup(bot):
    bot.add_cog(Fun(bot))