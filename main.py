import discord
from discord.ext import commands
from discord import Embed, Color
from discord.ext.commands import has_permissions, MissingPermissions
from keep_alive import keep_alive 


#Hide Secrets
import os

token = os.getenv("TOKEN")



client = commands.Bot(command_prefix="%", description="Learn Thunder Breathing", case_insensitive=True,  help_command=None)

for filename in os.listdir(f"./cogs"):
 if filename.endswith(f".py"):
  client.load_extension(f"cogs.{filename[:-3]}")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="雷の呼吸"))
    print('I have logged in as {0.user}'.format(client))

@client.command()
async def ping(ctx):
     await ctx.send(f'Pong! **{round(client.latency * 1000)} ms**!')

keep_alive()
client.run(token)