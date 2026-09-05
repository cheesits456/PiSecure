import discord
import os

from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ["botToken"]
serverID = os.environ["serverID"]

intents = discord.Intents.default()
intents.message_content = True

class Bot(commands.Bot):
    async def setup_hook(self) -> None:
        server = discord.Object(id=serverID)
        self.tree.copy_global_to(guild=server)
        await self.tree.sync(guild=server)

client = Bot(command_prefix="/", intents=intents)

@client.event
async def on_ready() -> None:
    print(f"Logged in as {client.user} ({client.user.id})")

@client.tree.command(name="list", description="List all files in the footage or framebuffer folders")
async def list(interaction: discord.Interaction) -> None:
    message = "_ _"
    await interaction.response.send_message(message)

@client.tree.command(name="still", description="Capture a still image and upload it to this channel")
async def still(interaction: discord.Interaction) -> None:
    await interaction.response.send_message(message)
    
client.run(TOKEN)