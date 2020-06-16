# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CawalmartItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    store = scrapy.Field()
    barcodes = scrapy.Field()
    sku = scrapy.Field()
    brand = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()
    package = scrapy.Field()
    image_url = scrapy.Field()
    category = scrapy.Field()
    link = scrapy.Field()
    branch = scrapy.Field()
    stock = scrapy.Field()
    price = scrapy.Field()
    pass
