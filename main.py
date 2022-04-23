import os
from discord.ext import commands
import discord
from flask import Flask
from threading import Thread
from Utils.config import get_token
from Utils import db

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=db.get_prefix_for_bot, intents=intents)
bot.remove_command("help")

os.system("title dabu BOT")
print("****************************************************************")
print("* Copyright of dabu, 2021                                      *")
print("* https://www.green-play.cz                                    *")
print("* https://www.youtube.com/channel/UCwKdMABJXncgE7PKtzuvDUQ     *")
print("****************************************************************")
print(f"""     _       _             ____   ____ _______
    | |     | |           |  _ \ / __ \__   __|
  __| | __ _| |__  _   _  | |_) | |  | | | |
 / _` |/ _` | '_ \| | | | |  _ <| |  | | | |
| (_| | (_| | |_) | |_| | | |_) | |__| | | |
 \__,_|\__,_|_.__/ \__,_| |____/ \____/  |_|
""")

@bot.event
async def on_ready():

    await bot.change_presence(activity=discord.Game("Miky BOT V1"))
    print('>────────────────────────<')
    print('Logged as:')
    print('Name: {0.user.name}'.format(bot))
    print('ID: {0.user.id}'.format(bot))
    print('>────────────────────────<')

    db.setup()
    for filename in os.listdir('./Modules'):
        if filename.endswith('.py'):
            bot.load_extension(f'Modules.{filename[:-3]}')

@bot.command()
async def setprefix(ctx,prefix):
    db.setprefix(ctx.guild.id, prefix)

from discord.ext import tasks
import json

@tasks.loop(seconds = 20)
async def api():
    with open('api/data.json', 'r') as f:
        data = json.load(f)
    members = 0
    channels = 0
    for item in bot.guilds:
        members += item.member_count
    for guild in bot.guilds:
        for channel in guild.text_channels:
            channels += 1
    for guild in bot.guilds:
        for channel in guild.voice_channels:
            channels += 1

        
    data["guilds"] = f"{len(list(bot.guilds))}"
    data["members"] = f"{members}"
    data["channels"] = f"{channels}"

    with open('api/data.json', 'w') as f:
        json.dump(data, f, indent=4)

# api.start()

bot.run(get_token())