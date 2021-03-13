from datetime import datetime
from goldscraper.priceInfo import PriceInfo

class PriceInfoCollection():
    """description of class"""
    def __init__(self):
        self.priceInfos = []
        self.lastUpdated = datetime.min

    def add(self, priceInfo: PriceInfo):
        self.priceInfos.append(priceInfo)
        self.lastUpdated = datetime.utcnow()

    def remove(self, priceInfo: PriceInfo):
        self.priceInfos.remove(priceInfo)
    
    def isEmpty(self):
        return not self.priceInfos

    def clear(self):
        self.priceInfos.clear()

    