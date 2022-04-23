import discord
from discord.ext import commands
import discord.utils
import json
from dotenv import load_dotenv
import os
import asyncio
import discord
from discord.ext import commands
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
import os
from discord.ext.commands import has_permissions
load_dotenv()

FOOTER = os.getenv('FOOTER')
ICON = os.getenv('ICON_URL')
class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self,member):
        with open('db/welcomer/joinch_id.json', 'r') as f:
          chid = json.load(f)
        if chid[str(member.guild.id)] == "None":
            channel = self.bot.get_channel(id=int(chid[str(member.guild.id)]))
        else:
            channel = self.bot.get_channel(id=int(chid[str(member.guild.id)]))
            welcome = Image.open('img/card.png')
            asset = member.avatar_url_as(size=128)
            data = BytesIO(await asset.read())
            pfp = Image.open(data)
            pfp = pfp.resize((258, 258))
            welcome.paste(pfp, (421, 62))
            font = ImageFont.truetype("fonts/Minecraft.otf", 35)
            font2 = ImageFont.truetype("fonts/Minecraft.otf", 40)
            d = ImageDraw.Draw(welcome)
            d.text((150, 381), f"{member.name}#{member.discriminator} just joined to the server", fill="white", anchor="ls", font=font2)
            d.text((456, 427), f"Member #{member.guild.member_count}", fill="gray", anchor="ls", font=font)
            welcome.save('img/pcard.png')
            await channel.send(f"Hey {member.mention} welcome to {member.guild.name}!",file = discord.File('img/pcard.png'))
            os.remove('img/pcard.png')

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        with open('db/welcomer/leavech_id.json', 'r') as f:
          chid = json.load(f)
        if chid[str(member.guild.id)] == "None":
            channel = self.bot.get_channel(id=int(chid[str(member.guild.id)]))
        else:
            channel = self.bot.get_channel(id=int(chid[str(member.guild.id)]))
            embed=discord.Embed(title=f"{member.name} has left", description=f"on server is {len(list(member.guild.members))} members", color=0xFF0000)
            embed.set_thumbnail(url=f"{member.avatar_url}")
            embed.set_footer(text=FOOTER, icon_url=ICON)
            await channel.send(embed=embed)

    @commands.command()
    @has_permissions(administrator=True)
    async def setjoinchannel(self,ctx,*, joinch:discord.TextChannel):
        with open('db/welcomer/joinch_id.json', 'r') as f:
            chid = json.load(f)

        chid[str(ctx.guild.id)] = joinch.id

        with open('db/welcomer/joinch_id.json', 'w') as f:
            json.dump(chid, f, indent=4)

        await ctx.send(f'Channel changed to: {joinch.mention}')

    @commands.command()
    @has_permissions(administrator=True)
    async def setleavechannel(self,ctx,*, leavech:discord.TextChannel):
        with open('db/welcomer/leavech_id.json', 'r') as f:
            chid = json.load(f)
       
        chid[str(ctx.guild.id)] = leavech.id

        with open('db/welcomer/leavech_id.json', 'w') as f:
            json.dump(chid, f, indent=4)

        await ctx.send(f'Channel changed to: {leavech.mention}')

    @commands.command()
    @has_permissions(administrator=True)
    async def disjoinchannel(self,ctx):
        with open('db/welcomer/joinch_id.json', 'r') as f:
            chid = json.load(f)

        chid[str(ctx.guild.id)] = "None"

        with open('db/welcomer/joinch_id.json', 'w') as f:
            json.dump(chid, f, indent=4)

        await ctx.send(f'Join channel disabled')

    @commands.command()
    @has_permissions(administrator=True)
    async def disleavechannel(self,ctx):
        with open('db/welcomer/leavech_id.json', 'r') as f:
            chid = json.load(f)
       
        chid[str(ctx.guild.id)] = "None"

        with open('db/welcomer/leavech_id.json', 'w') as f:
            json.dump(chid, f, indent=4)

        await ctx.send(f'Leave channel disabled')

def setup(bot):
    bot.add_cog(Welcome(bot))