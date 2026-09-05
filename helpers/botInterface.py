import discord
import os

from discord.ext import commands
from dotenv import load_dotenv


def sort_frame_list_by_number(filename):
    return int(filename.split(".")[0])


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

@client.tree.command(name="still", description="Upload the most recently captured frame to the current channel")
async def still(interaction: discord.Interaction) -> None:
    files = os.listdir("./framebuffer")
    files.sort(key=sort_frame_list_by_number)
    print(files)
    # await interaction.response.send_message(file=discord.File(""))
    
client.run(TOKEN)