# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

#from optparse import TitledHelpFormatter
import scrapy


class SeamsfriendlyItem(scrapy.Item):
    # define the fields for your item here like:
    Title = scrapy.Field()
    Price = scrapy.Field()
    Description = scrapy.Field()
    href = scrapy.Field()

    
