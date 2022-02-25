#!/usr/bin/env python3

import discord
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta

# print(str(dt_now))
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILDID = os.getenv("DISCORD_GUILD_ID")

intents = discord.Intents.all()
intents.typing = False
bot = discord.Bot(intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user}")


@bot.slash_command(guild_ids=[GUILDID])
async def hello(ctx):
    await ctx.respond("Hello.")


@bot.event
async def on_message(msg):
    if msg.content.startswith("!d bump"):
        dt_now = datetime.now()
        next_dt = dt_now + timedelta(hours=2)
        await msg.channel.send(f"Next: {str(next_dt)}")


bot.run(TOKEN)
