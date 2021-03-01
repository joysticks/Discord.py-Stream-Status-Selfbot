import discord
from discord.ext import commands

client = commands.Bot(command_prefix = ".", self_bot = True)

@client.event
async def on_ready():
    activity = discord.Streaming(name="Stream title here", url = "Twitch/youtube link here")
    await client.change_presence(status=discord.Status.idle, activity=activity)

client.run("discord token here", bot = False)