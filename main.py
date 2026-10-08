import discord 
import nick_changer
with open("token.txt") as file:
    token = file.read().strip()

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)
tree.add_command(nick_changer.nick)

@client.event
async def on_ready():
    await tree.sync()
    print(f"we have logged in as {client.user}")


client.run(token)   