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
@app_commands.describe(folder="Which folder to list the contents of")
async def list(interaction: discord.Interaction, folder: str) -> None:
    command = f"ls {folder}" if folder == "framebuffer" else f"tree {folder}"
    res = subprocess.run(
        args = command,
        executable = "/bin/bash",
        shell = True,
        capture_output = True,
        text = True
    )
    result = res.stdout
    match folder:
        case "framebuffer":
            result = result.split("\n")
            fileCount = len(res.stdout.split("\n")) - 1
            result.sort(key=sort_frame_list_by_number)
            result = "\n".join([
                f"├── {result[1]}",
                "│",
                "│     |",
                "│     v",
                "│",
                f"└── {result[-1]}",
                "",
                f"1 directory, {fileCount} file{"" if fileCount == 1 else "s"}"
            ])
        case "footage":
            result = result.split("\n",1)[1].split("\n")
            lastLine = result[-2].split(" ")
            lastLine[0] = str(int(lastLine[0]) - 1)
            result[-2] = " ".join(lastLine)
            result = "\n".join(result)
    await interaction.response.send_message(f"```js\n'{folder}'\n{result}```")



@client.tree.command(name="still", description="Upload the most recently captured frame to the current channel")
async def still(interaction: discord.Interaction) -> None:
    frameList = os.listdir("./framebuffer")
    frameList.sort(key=sort_frame_list_by_number)
    # Uploading the second-to-last frame because the most recent one might still be going through post-processing
    filePath = f"./framebuffer/{frameList[-2]}"
    await interaction.response.send_message(file=discord.File(filePath))



@client.tree.command(name="upload", description="Upload the specified file to the current channel")
@app_commands.describe(file="Which file to upload")
async def upload(interaction: discord.Interaction, file: str) -> None:
    await interaction.response.send_message(file)



client.run(TOKEN)