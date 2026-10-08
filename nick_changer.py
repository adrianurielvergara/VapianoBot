import discord 
from discord import app_commands

@app_commands.command(name="nick", description="Changes the nicknames")
async def nick(interaction: discord.Interaction, user: discord.Member, new_nickname: str):
    await user.edit(nick=new_nickname)
    await interaction.response.send_message(f"Nickname changed to {new_nickname}")

