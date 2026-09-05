import discord
import os
import subprocess

from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

from config import serverID
from helpers.functions import sort_frame_list_by_number


load_dotenv()
TOKEN = os.environ["botToken"]

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



@client.tree.command(name="list", description="List all files in the specified directory in a fancy file-tree")
@app_commands.choices(folder=[
    app_commands.Choice(name="Framebuffer", value="framebuffer"),
    app_commands.Choice(name="Footage", value="footage")
])
async def list(interaction: discord.Interaction, folder: str) -> None:
    res = subprocess.run(
        args = f"tree {folder}",
        executable = "/bin/bash",
        shell = True,
        capture_output = True,
        text = True
    )
    result = res.stdout.split("\n",1)[1].split("\n")
    lastLine = result[-2].split(" ")
    lastLine[0] = str(int(lastLine[0]) - 1)
    result[-2] = " ".join(lastLine)
    tree = "\n".join(result)
    await interaction.response.send_message(f"```ini\n[{folder}]\n{tree}```")



@client.tree.command(name="still", description="Upload the most recently captured frame to the current channel")
async def still(interaction: discord.Interaction) -> None:
    frameList = os.listdir("./framebuffer")
    frameList.sort(key=sort_frame_list_by_number)
    # Uploading the second-to-last frame because the most recent one might still be going through post-processing
    filePath = f"./framebuffer/{frameList[-2]}"
    await interaction.response.send_message(file=discord.File(filePath))



client.run(TOKEN)