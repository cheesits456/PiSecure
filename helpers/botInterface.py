import discord
import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ["botToken"]

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready() -> None:
    print(f"Logged in as {client.user} ({client.user.id})")

@client.command()
async def ping(ctx: commands.Context) -> None:
    """Reply with the bot's websocket latency."""
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")
    
client.run(TOKEN)