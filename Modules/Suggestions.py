import os
import time
import json
from discord.ext import commands
import discord
from discord.ext import commands
import os
from discord.ext.commands import has_permissions
import json
import discord
from discord.ext import commands
import discord.utils
import json
from dotenv import load_dotenv
import os
import discord
from discord.ext import commands
import os
import time
from dotenv import load_dotenv

load_dotenv()
import time
FOOTER = os.getenv('FOOTER')
ICON = os.getenv('ICON_URL')


class Suggestions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.emoji = ['1\u20e3', '2\u20e3', '3\u20e3', '4\u20e3', '5\u20e3',
                      '6\u20e3', '7\u20e3', '8\u20e3', '9\u20e3', '\U0001F51F']
    
    @commands.command()
    @has_permissions(administrator=True)
    async def setsugchannel(self,ctx,*, sugch:discord.TextChannel):
        with open('db/sugchid.json', 'r') as f:
            chid = json.load(f)

        chid[str(ctx.guild.id)] = sugch.id

        with open('db/sugchid.json', 'w') as f:
            json.dump(chid, f, indent=4)

        await ctx.send(f'Channel changed to: {sugch.mention}')

    @commands.command()
    @has_permissions(administrator=True)
    async def dissugchannel(self,ctx):
        with open('db/sugchid.json', 'r') as f:
            chid = json.load(f)
       
        chid[str(ctx.guild.id)] = "None"

        with open('db/sugchid.json', 'w') as f:
            json.dump(chid, f, indent=4)

        await ctx.send(f'Suggestions channel disabled')

    @commands.command(aliases=["sug"])
    async def suggest(self, ctx, *,suggestion):
        await ctx.message.delete()
        with open('db/sugchid.json', 'r') as f:
            chid = json.load(f)
        if chid[str(ctx.guild.id)] == 'None':
            msg = await ctx.send(f'Suggestions is disabled on this server')
            time.sleep(3)
            await msg.delete()
            
        else:    
            with open('db/sugchid.json', 'r') as f:
                chid = json.load(f)

            channel = self.bot.get_channel(id=int(chid[str(ctx.guild.id)]))

            em=discord.Embed(title="", description=f"{suggestion}", color=0x00ff00)
            em.set_author(name=f"{ctx.message.author}", icon_url=f"{ctx.author.avatar_url}")
            em.set_footer(text=FOOTER, icon_url=ICON)

            message = await channel.send(embed=em)
            await message.add_reaction("✅")
            await message.add_reaction("❌")



def setup(bot):
    bot.add_cog(Suggestions(bot))