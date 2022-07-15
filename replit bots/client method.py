import discord
import os

TOKEN = os.environ["token"]
client = discord.Client()

client.run(TOKEN)
