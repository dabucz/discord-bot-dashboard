import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
load_dotenv()
import json
FOOTER = os.getenv('FOOTER')
ICON = os.getenv('ICON_URL')

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['?'])
    async def help(self,ctx, command=None):
      with open('db/prefixes.json', 'r') as f:
          prefix = json.load(f)
      
      if not command:
          helpcommands=discord.Embed(title="ᕼᗴᒪᕈ", description="", color=0x00ff00)
          helpcommands.add_field(name=f":exclamation: `{prefix[str(ctx.guild.id)]}help info`", value="info commands", inline=True)
          helpcommands.add_field(name=f":name_badge: `{prefix[str(ctx.guild.id)]}help mod`", value="moderation commands", inline=True)
          helpcommands.add_field(name=f"<a:fun:863113337948078110> `{prefix[str(ctx.guild.id)]}help fun`", value="fun commands", inline=True)
          helpcommands.add_field(name=f":camera: `{prefix[str(ctx.guild.id)]}help image`", value="image commands", inline=True)
          helpcommands.add_field(name=f":question: `{prefix[str(ctx.guild.id)]}help sug`", value="suggestion commands", inline=True)
          helpcommands.add_field(name=f"`{prefix[str(ctx.guild.id)]}help welcome`", value="welcomer commands", inline=True)
          helpcommands.add_field(name=f"<a:giveway:863110974918754365> `{prefix[str(ctx.guild.id)]}help giveaway`", value="giveaway commands", inline=True)
          helpcommands.add_field(name=f":gear: `{prefix[str(ctx.guild.id)]}help config`", value="config commands", inline=True)
          helpcommands.set_footer(text=FOOTER, icon_url=ICON)

      if command == "info":
          helpcommands=discord.Embed(title=":exclamation: Info commands", description="", color=0x00ff00)
          helpcommands.add_field(name=f"`{prefix[str(ctx.guild.id)]}ping`", value="bot ping", inline=True)
          helpcommands.add_field(name=f"`{prefix[str(ctx.guild.id)]}stauts`", value="bot status", inline=True)
          helpcommands.add_field(name=f"`{prefix[str(ctx.guild.id)]}serverinfo`", value="server info", inline=True)
          helpcommands.set_footer(text=FOOTER, icon_url=ICON)

      if command == "mod":
          helpcommands = discord.Embed(title=":name_badge: Moderation Help",description="",color=0x00ff00)
          helpcommands.add_field(name=f"`{prefix[str(ctx.guild.id)]}kick <name>`",value="kick member",inline=True)
          helpcommands.add_field(name=f"`{prefix[str(ctx.guild.id)]}ban <name> <reason>`",value="ban user",inline=True)
          helpcommands.add_field(name=f"`{prefix[str(ctx.guild.id)]}clear <number>`",value="clear number of messages",inline=True)
          helpcommands.add_field(name=f"`{prefix[str(ctx.guild.id)]}mute <name>`",value="mute user",inline=True)
          helpcommands.add_field(name=f"`{prefix[str(ctx.guild.id)]}unmute <name>`",value="unmute user",inline=True)
          helpcommands.add_field(name=f"`{prefix[str(ctx.guild.id)]}addrole <name> <role>`",value="add role to user",inline=True)
          helpcommands.add_field(name=f"`{prefix[str(ctx.guild.id)]}removerole <name> <role>`",value="remove role from user",inline=True)
          helpcommands.add_field(name=f"`{prefix[str(ctx.guild.id)]}slowmode <seconds>`",value="set slowmode",inline=True)
          helpcommands.set_footer(text=FOOTER, icon_url=ICON)

      if command == "fun":
          helpcommands = discord.Embed(title="<a:fun:863113337948078110> Fun Help", description="", color=0x00ff00)
          helpcommands.add_field(name=f"`{prefix[str(ctx.guild.id)]}pp (name)`",value="i will show you how long you have peepee",inline=True)
          helpcommands.add_field(name=f"`{prefix[str(ctx.guild.id)]}howgay <name>`",value="how many % is the member gay",inline=True)
          helpcommands.add_field(name=f"`{prefix[str(ctx.guild.id)]}say <message>`",value="i will say what you want to say",inline=True)
          helpcommands.add_field(name=f"`{prefix[str(ctx.guild.id)]}hack <member>`",value="i will hack member",inline=True)
          helpcommands.set_footer(text=FOOTER, icon_url=ICON)

      if command == "image":
          helpcommands = discord.Embed(title=":camera: Images Help", description="", color=0x00ff00)
          helpcommands.add_field(name=f"`{prefix[str(ctx.guild.id)]}wanted <name>`", value="This command create wanted foto")
          helpcommands.add_field(name=f"`{prefix[str(ctx.guild.id)]}rip <name>`", value="This command create rip foto")
          helpcommands.set_footer(text=FOOTER, icon_url=ICON)

      if command == "sug":
          helpcommands = discord.Embed(title=":question: Suggestions Help", description="", color=0x00ff00)
          helpcommands.add_field(name=f"`{prefix[str(ctx.guild.id)]}sug <suggestion>`", value="Sends suggestion to channel")
          helpcommands.add_field(name=f"`{prefix[str(ctx.guild.id)]}setsugchannel <channel>`", value="Admin only! set channel for suggestions")
          helpcommands.set_footer(text=FOOTER, icon_url=ICON)

      if command == "welcome":
          helpcommands = discord.Embed(title="Welcome Help", description="", color=0x00ff00)
          helpcommands.add_field(name=f"`{prefix[str(ctx.guild.id)]}setjoinchannel <channel>`", value="Admin only! set channel for join message")
          helpcommands.add_field(name=f"`{prefix[str(ctx.guild.id)]}setleavechannel <channel>`", value="Admin only! set channel for leave message")
          helpcommands.add_field(name=f"`{prefix[str(ctx.guild.id)]}disjoinchannel`", value="Admin only! Disable join channel")
          helpcommands.add_field(name=f"`{prefix[str(ctx.guild.id)]}disleavechannel`", value="Admin only! Disable leave channel")
          helpcommands.set_footer(text=FOOTER, icon_url=ICON)

      if command == "config":
          helpcommands = discord.Embed(title=":gear: Config Help", description=f"", color=0x00ff00)
          helpcommands.add_field(name=f"Enable", value=f"`{prefix[str(ctx.guild.id)]}setjoinchannel <channel>` Admin only! set channel for join message\n`{prefix[str(ctx.guild.id)]}setleavechannel <channel>` Admin only! set channel for leave message\n`{prefix[str(ctx.guild.id)]}setsugchannel <channel>` Admin only! set channel for suggestions\n`{prefix[str(ctx.guild.id)]}setprefix <prefix>` Admin only! change my prefix on guild", inline=True)
          helpcommands.add_field(name=f"Disable", value=f"`{prefix[str(ctx.guild.id)]}disjoinchannel` Admin only! Disable join channel\n`{prefix[str(ctx.guild.id)]}disleavechannel` Admin only! Disable leave channel\n`{prefix[str(ctx.guild.id)]}dissughannel` Admin only! Disable suggestions channel", inline=True)
          helpcommands.set_footer(text=FOOTER, icon_url=ICON)

      if command == "giveaway":
          helpcommands = discord.Embed(title="<a:giveway:863110974918754365>Giveaways Help", description="", color=0x00ff00)
          helpcommands.add_field(name=f"`{prefix[str(ctx.guild.id)]}gstart <time> <prize>`", value="Starts giveaway")
          helpcommands.set_footer(text=FOOTER, icon_url=ICON)

      await ctx.send(embed=helpcommands)

def setup(bot):
    bot.add_cog(Help(bot))