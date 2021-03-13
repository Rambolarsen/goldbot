import unittest
from g2gScraper import Scraper


class ScraperTest(unittest.TestCase):
    def test_print_update(self):
        scraper = Scraper('https://www.g2g.com/wow-classic-eu/gold-27815-27817?server=33751&faction=33739&sorting=lowest_price')
        self.assertIsNotNone(scraper.get_gold_prices())