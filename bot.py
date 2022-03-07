
import scrapy
from ..items import SeamsfriendlyItem

class BotSpider(scrapy.Spider):
    
    name = 'bot'
    count = 1
    #allowed_domains = ['example.com']
    start_urls = ["https://in.seamsfriendly.com/collections/new-arrivals?page=2"]

    def parse(self, response):
        items = SeamsfriendlyItem() 
        items["Title"] = response.css("h2.ProductItem__Title.Heading a::text").extract()
        items["Price"] = price = response.css("div.ProductItem__PriceList.Heading span::text").extract()
        items["Description"] = response.css("div.label_icon.label_icon-mob.orgc::text").extract()
        items["href"] = response.css("div.ProductItem__Wrapper a::attr(href)").extract()
        yield items

        BotSpider.count += 1
        next_page = "https://in.seamsfriendly.com/collections/new-arrivals?page="+str(BotSpider.count)
        if BotSpider.count <= 5:
            yield response.follow(next_page,callback = self.parse)
    