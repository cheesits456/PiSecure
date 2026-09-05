import discord
import os
import subprocess

from discord import app_commands
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


@client.tree.command()
@app_commands.choices(folder=[
    app_commands.Choice(name="Framebuffer", value="framebuffer"),
    app_commands.Choice(name="Footage", value="footage")
])
async def list(interaction: discord.Interaction, folder: str) -> None:
    result = subprocess.run(
        args = f"tree {folder}",
        executable = "/bin/bash",
        shell = True,
        capture_output = True, # Python >= 3.7 only
        text = True
    )
    await interaction.response.send_message(f"```{result.stdout}```")

@client.tree.command(name="still", description="Upload the most recently captured frame to the current channel")
async def still(interaction: discord.Interaction) -> None:
    frameList = os.listdir("./framebuffer")
    frameList.sort(key=sort_frame_list_by_number)
    # Uploading the second-to-last frame because the most recent one might still be going through post-processing
    filePath = f"./framebuffer/{frameList[-2]}"
    await interaction.response.send_message(file=discord.File(filePath))
    
client.run(TOKEN)