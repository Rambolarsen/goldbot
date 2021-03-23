# bot.py
import os

from discord.ext import commands
from dotenv import load_dotenv
from goldscraper.scraper import Scraper
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

BOT = commands.Bot(command_prefix='!')

FIREMAWGOLDPRICES = Scraper('https://www.g2g.com/wow-classic-eu/gold-27815-27817?server=33751&faction=33739&sorting=lowest_price')

@BOT.group(name='price', invoke_without_command=True, aliases=['p'])
async def price_cmd(ctx):
    for price in FIREMAWGOLDPRICES.get_gold_prices():
        await ctx.send(price)   
    
BOT.run(TOKEN)
