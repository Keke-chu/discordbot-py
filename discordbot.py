from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == f'{PREFIX}양지윤':
        await message.channel.send("바보")

    if message.content.startswith(f'{PREFIX}케이루'):
        await message.channel.send('안녕하세요?')

@bot.command()
async def play(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    
try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
