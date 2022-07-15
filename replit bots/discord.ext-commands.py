from discord.ext import commands
import os

bot = commands.Bot(command_prefix="-")#make prefix whatever you want
token = os.environ["token"]#make sure you  have a secret in replit with your bots token. name it whatever you want
