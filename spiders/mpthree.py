import scrapy
# from scrapy.loader import Itemloader
# from .dwnldmp.items import Dwnlditem


class MpthreeSpider(scrapy.Spider):
    name = 'mpthree'
    #allowed_domains = ['x']
    start_urls = [
        'https://www.poornalayam.org/classes-recorded/brahma-sutram/']

    def parse(self, response):
        lnks = response.xpath(
            "//following::tr[2]/td[2]/a[contains(@href,'mp3')]")
        for lnk in lnks:
            print(lnk)
