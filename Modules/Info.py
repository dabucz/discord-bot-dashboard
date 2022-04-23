from discord.ext import commands
import os
import discord
from dotenv import load_dotenv

load_dotenv()
import time
FOOTER = os.getenv('FOOTER')
ICON = os.getenv('ICON_URL')

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def status(self,ctx):
        await ctx.send("https://stats.uptimerobot.com/LWDlQtPxLg")
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")

    @commands.command()
    async def serverinfo(self,ctx):
      name = str(ctx.guild.name)
      description = str(ctx.guild.description)

      owner = str(ctx.guild.owner)
      id = str(ctx.guild.id)
      region = str(ctx.guild.region)
      memberCount = str(ctx.guild.member_count)

      icon = str(ctx.guild.icon_url)

      embed = discord.Embed(title=name + " Server Information",description=description,color=0x00ff00)
      embed.set_thumbnail(url=icon)
      embed.add_field(name="Owner", value=owner, inline=True)
      embed.add_field(name="Server ID", value=id, inline=True)
      embed.add_field(name="Region", value=region, inline=True)
      embed.add_field(name="Member Count", value=memberCount, inline=True)

      await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_cog(Info(bot))