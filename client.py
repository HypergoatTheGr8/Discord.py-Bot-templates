import discord
import os

#this is repl.it version, so make sure you have a secret with your token in it. you can name it whatever you want
token = os.environ["token"]
client = discord.Client()
bot = "Bot_template#1234"

@client.event
async def on_ready():
  print(f"{bot} is ready!")
  
@client.event
async def on_message(message):
  if message.content.startswith("+hello"):
    await message.channel.send("hi there!")
    
  elif message.content.startswith("+quote"):
    
