# -*- coding: utf-8 -*-
import scrapy

from scrapy.crawler import CrawlerProcess
from multiprocessing import Process, Queue
from twisted.internet import reactor
from scrapy.settings import Settings
import re,ast

import json
import re

class CaWalmartSpider(scrapy.Spider):

    start_urls = []

    def __init__(self, *args, **kwargs):

        super(CaWalmartSpider, self).__init__(*args, **kwargs)

        # Set start_urls and total page crawler
        self.start_urls = ["https://www.walmart.ca/en/grocery/fruits-vegetables/fruits/N-3852"]
    
    name = 'ca_walmart'

    # Start request with first url initalize
    def start_requests(self):
        # get item inf
        for eachPageURL in self.start_urls:
            yield scrapy.Request(eachPageURL, callback=self.getItemInformationDetail,
                                    errback=self.errback_httpbin,
                                    dont_filter=True)

    # Get the information for each item in fruits
    def getItemInformationDetail(self, response):

        print(response.text)
        json_data = response.css('script::text')[6].get()
        json_data = json_data[27:]
        json_data = json_data[:-1]
        json_data = json.loads(json_data)

        productId = json_data["product"]["activeSkuId"]
        # Product Store
        productStore = json_data["entities"]["skus"][productId]["endecaDimensions"][7]["value"]

        # Product SKU
        productSKU = re.search(r'"sku":"(\d+)',response.text).groups()[0]

        # Product bar code
        productBarCode = ast.literal_eval(re.search(r'"upc":(\[.*?\])',response.text).groups()[0])

        # Product brand
        productBrand = json_data["entities"]["skus"][productId]["brand"]["name"]

        # Product name
        productName = json_data["entities"]["skus"][productId]["name"]

        productDescription = json_data["entities"]["skus"][productId]["longDescription"]

        print("=======================================================================")
        print("Product URL: " + response.url)
        print("Product Store: " + productStore)
        print("Product SKU: " + productSKU)
        print("Product Bar code: " + str(productBarCode))
        print("Product Brand: " + productBrand)
        print("Product Name: " + productName)
        print("Product Description: " + productDescription)
        print("=======================================================================")
    
    def errback_httpbin(self, failure):
        # log all failures
        self.logger.error(repr(failure))

crawler_settings = Settings()
process = CrawlerProcess(settings=crawler_settings)
process.start()
