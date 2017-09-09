#-*- coding: utf-8 -*- 
from scrapy.loader import ItemLoader
from parlament.items import ParlamentItem
from scrapy.loader.processors import MapCompose

import scrapy

class BasicSpider(scrapy.Spider):
    name = "basic"
    allowed_domains = ["http://www.parlament.rs"]
    start_urls = ['http://www.parlament.rs/BAL%C5%A0A_BO%C5%BDOVI%C4%86.559.891.html']
    def parse(self, response):
        
        l = ItemLoader(item=ParlamentItem(), response=response)
        l.add_xpath('ime', '//h2/text()', MapCompose(lambda i: i.replace('\n', ''), str.strip, str.capitalize))
        l.add_xpath('prezime', '//h2/span/text()', MapCompose(str.capitalize))
        l.add_xpath('stranka', '//h4[contains(text(), "stranka")]/following::p[1]/text()', MapCompose(lambda i: i.replace('\n', ''), str.strip,))
        l.add_xpath('posl_grupa', '//h4[contains(text(), "grupa")]/following::p[1]/a/text()')
        l.add_xpath('mesto', '//h4[contains(text(), "Mesto")]/following::p[1]/text()')
        l.add_xpath('zanimanje', '//h4[contains(text(), "Zanimanje")]/following::p[1]/text()')
        l.add_xpath('godina', '//h4[contains(text(), "Godina")]/following::p[1]/text()')
        l.add_xpath('foto','//div[@class = "image_holder left"]/img/@src')
        l.add_xpath('twitter','//ul[@class = "social-list"]/li[1]/a/@href')
        l.add_xpath('facebook','//ul[@class = "social-list"]/li[2]/a/@href')
        
        return l.load_item()