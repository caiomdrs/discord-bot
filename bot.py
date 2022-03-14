import discord
import time

client = discord.Client()


@client.event
# print when bot is ready
async def on_ready():
    print("Online!")


@client.event
async def on_message(message):
    # Add reaction on messages
    emoji = '\N{THUMBS UP SIGN}'
    await message.add_reaction(emoji)

    # print message on terminal
    print(f"Name:{message.author.name}, ID: {message.author.id}, Mensagem: {message.content}")

    # Say hello when someone say Hi on server
    if message.content.startswith("Hi"):
        await message.channel.send("Hello")

# run bot
client.run("YOUR BOT TOKEN")
