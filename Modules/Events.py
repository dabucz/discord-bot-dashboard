from discord.ext import commands
from Utils.db import register_guild, unregister_guild

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        register_guild(guild.id)

    @commands.Cog.listener()
    async def on_guild_remove(self,guild):
        unregister_guild(guild.id)

def setup(bot):
    bot.add_cog(Events(bot))