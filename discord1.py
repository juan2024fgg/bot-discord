import discord
from discord.ext import commands
intents = discord.Intents.default()

intents.message_content = True
bot = commands.Bot(command_prefix="?",intents=intents)
client = discord.Client(intents=intents)

token = ""
@bot.event
async def on_ready():
    print(f"hola me llamo {bot.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("!hola"):
        await message.channel.send("hola, ¿En que puedo ayudarte?")
    elif message.content.startswith("!adios"):
        await message.channel.send("Adiosss!!1!1!")
    elif message.content.startswith("!eres dios?"):
        await message.channel.send(";)")
    elif message.content.startswith("!english or spanish?"):
        await message.channel.send("https://www.youtube.com/watch?v=hNCZh6Sh4jI")

client.run(token)            
