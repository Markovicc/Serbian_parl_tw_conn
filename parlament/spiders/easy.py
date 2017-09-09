# -*- coding: utf-8 -*-

import scrapy
from parlament.items import ParlamentItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader

class EasySpider(CrawlSpider):
    name = 'easy'
    allowed_domains = ['http://www.parlament.rs']
    start_urls = ['http://www.parlament.rs/narodna-skupstina-/sastav/narodni-poslanici/aktuelni-saziv.890.html']

    rules = (Rule(LinkExtractor (allow=('//strong')), callback='parse_item'),)

    def parse_item(self, response):
        l = ItemLoader(item=ParlamentItem(), response=response)
        l.add_xpath('ime', '//h2/text()')
        l.add_xpath('prezime', '//h2/span/text()')
        l.add_xpath('stranka', '//h4[contains(text(), "stranka")]/following::p[1]/text()')
        l.add_xpath('posl_grupa', '//h4[contains(text(), "grupa")]/following::p[1]/a/text()')
        l.add_xpath('mesto', '//h4[contains(text(), "Mesto")]/following::p[1]/text()')
        l.add_xpath('zanimanje', '//h4[contains(text(), "Zanimanje")]/following::p[1]/text()')
        l.add_xpath('godina', '//h4[contains(text(), "Godina")]/following::p[1]/text()')
        l.add_xpath('foto','//div[@class = "image_holder left"]/img/@src')
       
        
        
        return l.load_item()
