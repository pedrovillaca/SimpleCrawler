import scrapy
import requests
import json

class ItapuaSpider(scrapy.Spider):
    name = 'Itapua'
    allowed_domains = ['itapua.com.br']
    start_urls = ['https://itapua.com.br/']


    def parse(self, response):
        databox = response.xpath('*//div[@class="data-box"]') #seletor da div
        #response.selector.remove_namespaces()
        for d in databox:
            yield {
            'produto':d.xpath('.//div[@class="name-box"]/a/text()').getall(),
            'preco':d.xpath('.//span[@class="best-price"]/text()').getall()
            }

        arq = open('data.json', 'w')
        json.dump('produto', 'preco')
        arq.close()


