import requests
from bs4 import BeautifulSoup

from goldscraper.priceInfo import PriceInfo
from goldscraper.priceInfoCollection import PriceInfoCollection
from datetime import datetime, timedelta

class Scraper():
    def __init__(self, url: str = None): 
        self.url = url
        self.priceInfos = PriceInfoCollection()

    def get_gold_prices(self, count: int = 5):    
        self.refresh_if_outdated()
        if self.priceInfos.isEmpty():
            page = requests.get(self.url)
            soup = BeautifulSoup(page.content, 'html.parser')

            results = soup.find(id='product-listings')

            products = results.find_all('li', class_='products__list-item')
            
            for product in products:
                sellerName = product.find(class_='seller__name')        
                priceRow = product.find(class_='products__exch-rate input-gold')
                quantityRow = product.find(class_='products__statistic-amount')
                quantity = quantityRow.get('data-fc-qty')
                priceInfo = priceRow.find('span')
                price = PriceInfo(sellerName.text.strip(),priceInfo.text.strip(), quantity)
                self.priceInfos.add(price)  
                if len(self.priceInfos.priceInfos) >= count:
                    break        
        
        return self.formated_gold_prices()

    def formated_gold_prices(self):
        for priceInfo in self.priceInfos.priceInfos:
            yield priceInfo.print()

    def refresh_if_outdated(self):
        updateTreshold = self.priceInfos.lastUpdated + timedelta(hours=1)
        utcnow = datetime.utcnow()
        if updateTreshold < utcnow:
            self.priceInfos.clear()
