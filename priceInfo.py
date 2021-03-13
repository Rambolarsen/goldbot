from decimal import *

class PriceInfo():
    def __init__(self, seller: str = None , price: Decimal = None , quantity: int = None):
        self.seller = seller
        self.price = price
        self.quantity = quantity

    def print(self):
        return '```Price: {} Quantity: {} Seller: {}```'.format(self.price, self.quantity, self.seller)
