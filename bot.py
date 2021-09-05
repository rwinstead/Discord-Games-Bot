import os

import discord
from dotenv import load_dotenv
import random

curr_games = ["Chicken Horse", "Gun Game", "Factorio", "Golf", "For the King", "LoL", "Emulator", "Tabletop Sim", "Fall Guys", "Pummel Party", "Halo", "Hammerwatch", "Risk of Rain", "Sea of Thieves", "Unrailed", "Valheim", "Stick Fight", "Scribblio"]

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == "*games":
        await message.channel.send("""
            **Games in rotation:** \n • Chicken Horse \n • Gun Game \n • Factorio \n • Golf \n • For the King \n • League of Legends \n • Emulator \n • Tabletop Simulator \n • Fall Guys \n • Pummel Party \n • Halo \n • Hammerwatch \n • Risk of Rain \n • Sea of Thieves \n • Unrailed \n • Valheim \n • Scribblio \n • Stick Fight \n \n **Older stuff:**\n • Armello \n • Distance \n • Killing Floor \n • Borderlands
            """)

    if message.content.lower() == "*help":
        await message.channel.send("Available commands: *games, *random, *chill")

    if message.content.lower() == "*random":
        response = random.choice(curr_games)
        await message.channel.send(response)

    if message.content.lower() == "*chill":
        await message.channel.send("""**Chiller games:** \n • Golf \n • Fall Guys \n • Scribblio \n • Factorio \n • Halo \n • Sea of Thieves """)


client.run(TOKEN)