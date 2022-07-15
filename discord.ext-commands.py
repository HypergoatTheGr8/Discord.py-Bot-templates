from discord.ext import commands
import os

token = os.environ["token"]
bot = commands.Bot(command_prefix="-")#make the prefix whatever you want
