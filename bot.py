import discord
from discord.ext import commands
from discord import utils
import mysql.connector
from db import get_db_cursor, close_db_connection
from dotenv import load_dotenv
import random
from datetime import datetime, timedelta, timezone
from asyncio import Queue
import time
import asyncio
import requests
import os

load_dotenv()

db, cursor = get_db_cursor()

TOKEN = os.getenv("BOT_TOKEN")
PREFIX = os.getenv("BOT_PREFIX")

bot = commands.Bot(command_prefix=PREFIX, help_command=None, intents=discord.Intents.all())

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.members = True
intents.guilds = True
intents.dm_messages = True

@bot.event
async def on_ready():
    activity = discord.Game(f"!help")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"{ctx.author.mention}, command not found. Please check the command and try again!")

@bot.event
async def on_close():
    close_db_connection(db, cursor)

# Run the bot
bot.run(TOKEN)
