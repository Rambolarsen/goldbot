# bot.py
import os

from discord.ext import commands
from dotenv import load_dotenv
from goldscraper.scraper import Scraper
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

BOT = commands.Bot(command_prefix='!')

FIREMAWGOLDPRICES = Scraper('https://www.g2g.com/wow-classic-tbc/gold-29076-29077?faction=41397&server=41013&sorting=lowest_price')

@BOT.group(name='price', invoke_without_command=True)
async def price_cmd(ctx):
    for price in FIREMAWGOLDPRICES.get_gold_prices():
        await ctx.send(price)   
    
BOT.run(TOKEN)
