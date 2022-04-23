import os
import json
from discord.ext import commands
import discord
from discord.ext import commands
import os
import os
from discord.ext.commands import has_permissions, MissingPermissions
import json
from dotenv import load_dotenv

load_dotenv()
FOOTER = os.getenv('FOOTER')
ICON = os.getenv('ICON_URL')

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.emoji = ['1\u20e3', '2\u20e3', '3\u20e3', '4\u20e3', '5\u20e3',
                      '6\u20e3', '7\u20e3', '8\u20e3', '9\u20e3', '\U0001F51F']
    
    commands.sniped_messages = {}

    @commands.Cog.listener()
    async def on_message_delete(self,message):
        commands.sniped_messages[message.guild.id] = (message.content, message.author, message.channel.name, message.created_at)

    @commands.command()
    async def snipe(self,ctx):
        try:
            contents, author, channel_name, time = commands.sniped_messages[ctx.guild.id]
        
        except:
            await ctx.send("not found any message to snipe")
        
        embed= discord.Embed(description=contents, color=0x00FF00, timestamp=time)
        embed.set_author(name=f"{author.name}#{author.discriminator}", icon_url=author.avatar_url)
        embed.set_footer(text=f"Deleted in: #{channel_name}")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def addrole(self,ctx, member:discord.Member, role:discord.Role):
      await member.add_roles(role)
      embed = discord.Embed(title="added roles", description=f"added role to {member.mention}",colour=0x00FF00)
      embed.set_footer(text=FOOTER, icon_url=ICON)
      await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def removerole(self,ctx, member:discord.Member, role:discord.Role):
      await member.remove_roles(role)
      embed = discord.Embed(title="removed roles", description=f"removed role from {member.mention}",colour=0x00FF00)
      embed.set_footer(text=FOOTER, icon_url=ICON)
      await ctx.send(embed=embed)

# kick user
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self,ctx, member: discord.Member, *, reason=None):
      await member.kick(reason=reason)
      await ctx.send(f'User {member.mention} has kicked.')

# bans a user with a reason
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'User {member} has been banned for {reason}.')


    @commands.command(aliases=['c'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self,ctx, amount=2):
      await ctx.channel.purge(limit=amount + 1)

    @commands.command(description="Mutes the specified user.")
    @commands.has_permissions(manage_messages=True)
    async def mute(self,ctx, member: discord.Member, *, reason=None):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")

        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted", colour=discord.Colour(0xFF0000))

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
        embed = discord.Embed(title="muted", description=f"{member.mention} was muted ", colour=0xFF0000)
        embed.add_field(name="reason:", value=reason, inline=False)
        embed.set_footer(text=FOOTER, icon_url=ICON)
        await ctx.send(embed=embed)
        await member.add_roles(mutedRole, reason=reason)
        await member.send(f" you have been muted from: {guild.name} reason: {reason}")

    @commands.command(description="Unmutes a specified user.")
    @commands.has_permissions(manage_messages=True)
    async def unmute(self,ctx, member: discord.Member):
       mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

       await member.remove_roles(mutedRole)
       await member.send(f" you have unmuted from: {ctx.guild.name}")
       embed = discord.Embed(title="unmute", description=f" unmuted {member.mention}",colour=0x00FF00)
       embed.set_footer(text=FOOTER, icon_url=ICON)
       await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    @has_permissions(administrator=True)
    async def setprefix(self,ctx, prefix):
        with open('db/prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix

        with open('db/prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

        await ctx.send(f'Prefix changed to: {prefix}')
        await ctx.guild.me.edit(nick=f"{prefix}┃{self.bot.user.name}")
    
    @commands.command()
    @has_permissions(manage_channels=True)
    async def slowmode(self,ctx, seconds: int):
        await ctx.channel.edit(slowmode_delay=seconds)
        if seconds == 0:
            await ctx.send(f"Slowmode in this channel has disabled")
        else:
            await ctx.send(f"Slowmode in this channel set to {seconds}")
    @setprefix.error
    async def setprefix_error(self,ctx, error):
      if isinstance(error, MissingPermissions):
        await ctx.send(embed=discord.Embed(title="Sorry {}, you do not have permissions to do that!".format(ctx.message.author), description="", color=discord.Color.red()))
        
    @slowmode.error
    async def slowmode_error(self,ctx, error):
      if isinstance(error, MissingPermissions):
        await ctx.send(embed=discord.Embed(title="Sorry {}, you do not have permissions to do that!".format(ctx.message.author), description="", color=discord.Color.red()))
    @addrole.error
    async def addrole_error(self,ctx, error):
      if isinstance(error, MissingPermissions):
        await ctx.send(embed=discord.Embed(title="Sorry {}, you do not have permissions to do that!".format(ctx.message.author), description="", color=discord.Color.red()))

    @removerole.error
    async def removerole_error(self,ctx, error):
      if isinstance(error, MissingPermissions):
        await ctx.send(embed=discord.Embed(title="Sorry {}, you do not have permissions to do that!".format(ctx.message.author), description="", color=discord.Color.red()))

    @kick.error
    async def kick_error(self,ctx, error):
      if isinstance(error, MissingPermissions):
        await ctx.send(embed=discord.Embed(title="Sorry {}, you do not have permissions to do that!".format(ctx.message.author), description="", color=discord.Color.red()))

    @ban.error
    async def ban_error(self,ctx, error):
      if isinstance(error, MissingPermissions):
        await ctx.send(embed=discord.Embed(title="Sorry {}, you do not have permissions to do that!".format(ctx.message.author), description="", color=discord.Color.red()))
      
    @clear.error
    async def clear_error(self,ctx, error):
      if isinstance(error, MissingPermissions):
        await ctx.send(embed=discord.Embed(title="Sorry {}, you do not have permissions to do that!".format(ctx.message.author), description="", color=discord.Color.red()))

    @mute.error
    async def mute_error(self,ctx, error):
      if isinstance(error, MissingPermissions):
        await ctx.send(embed=discord.Embed(title="Sorry {}, you do not have permissions to do that!".format(ctx.message.author), description="", color=discord.Color.red()))

    @unmute.error
    async def unmute_error(self,ctx, error):
      if isinstance(error, MissingPermissions):
        await ctx.send(embed=discord.Embed(title="Sorry {}, you do not have permissions to do that!".format(ctx.message.author), description="", color=discord.Color.red()))




def setup(bot):
    bot.add_cog(Mod(bot))