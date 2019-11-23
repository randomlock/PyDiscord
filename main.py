import os

import discord
from dotenv import load_dotenv


load_dotenv()
client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'hi':
        await message.channel.send('hey')

if __name__ == '__main__':
    TOKEN = os.getenv('DISCORD_TOKEN')
    client.run(TOKEN)
