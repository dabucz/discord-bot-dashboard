
import discord
from discord.ext import commands
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO

import os


class Images(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rip(self, ctx, member: discord.Member=None):
      if not member:
        member = ctx.author

      rip = Image.open('img/rip.png')

      asset = member.avatar_url_as(size=128)
      data = BytesIO(await asset.read())
      pfp = Image.open(data)
      pfp = pfp.resize((500, 500))
      rip.paste(pfp, (255, 623))
      rip.save('img/prip.png')
      await ctx.send(file = discord.File('img/prip.png'))
      os.remove('img/prip.png')

    @commands.command()
    async def wanted(self, ctx, member: discord.Member=None):
      if not member:
        member = ctx.author

      rip = Image.open('img/wanted.jfif')

      asset = member.avatar_url_as(size=128)
      data = BytesIO(await asset.read())
      pfp = Image.open(data)
      pfp = pfp.resize((100, 100))
      rip.paste(pfp, (45, 89))
      rip.save('img/pwanted.png')
      await ctx.send(file = discord.File('img/pwanted.png'))
      os.remove('img/pwanted.png')

    @commands.command()
    async def w(self,ctx, member: discord.Member=None):
      if not member:
        member = ctx.author

      welcome = Image.open('img/welcome.jpg')
      asset = member.avatar_url_as(size=128)
      data = BytesIO(await asset.read())
      pfp = Image.open(data)
      
      pfp = pfp.resize((200, 200))
      welcome.paste(pfp, (29, 32))
      font = ImageFont.truetype("fonts/Minecraft.otf", 30)
      font2 = ImageFont.truetype("fonts/Minecraft.otf", 60)
      d = ImageDraw.Draw(welcome)
      d.text((25, 371), f"On server is {member.guild.member_count} Members!", fill="black", anchor="ls", font=font)
      d.text((326, 80), f"{member}", fill="black", anchor="ls", font=font)
      d.text((326, 54), f"Welcome!", fill="black", anchor="ls", font=font2)
      welcome.save('img/pwelcome.jpg')
      await ctx.send(file = discord.File('img/pwelcome.jpg'))
      os.remove('img/pwelcome.jpg')



def setup(bot):
    bot.add_cog(Images(bot))