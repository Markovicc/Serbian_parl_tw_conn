#-*- coding: utf-8 -*- 
from scrapy.loader import ItemLoader
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join
from parlament.items import ParlamentItem
import datetime
from scrapy.http import Request
from urllib.parse import urljoin

import scrapy

class BasicSpider(scrapy.Spider):
    
    name = "manual"
    allowed_domains = ["http://www.parlament.rs"]
    start_urls =['http://www.parlament.gov.rs/narodna-skupstina-/sastav/narodni-poslanici/aktuelni-saziv.890.html']
    
    def parse(self, response):
        
        selector = response.xpath('//strong//a/@href') 
        
        for url in selector.extract():
            adr = urljoin('http://www.parlament.rs', url)
            yield Request(adr, callback = self.parse_item, 
                          dont_filter=True) 
             
            
    
    
        
    def parse_item(self, response):
       
        l = ItemLoader(item=ParlamentItem(), response=response)
        l.add_xpath('ime', '//h2/text()', MapCompose(lambda i: i.replace('\n', ''), str.strip, str.capitalize))
        l.add_xpath('prezime', '//h2/span/text()', MapCompose(str.capitalize))
        l.add_xpath('stranka', '//h4[contains(text(), "stranka")]/following::p[1]/text()', MapCompose(lambda i: i.replace('\n', ''), str.strip,))
        l.add_xpath('posl_grupa', '//h4[contains(text(), "grupa")]/following::p[1]/a/text()')
        l.add_xpath('mesto', '//h4[contains(text(), "Mesto")]/following::p[1]/text()')
        l.add_xpath('zanimanje', '//h4[contains(text(), "Zanimanje")]/following::p[1]/text()')
        l.add_xpath('godina', '//h4[contains(text(), "Godina")]/following::p[1]/text()')
        l.add_xpath('foto','//div[@class = "image_holder left"]/img/@src')
        l.add_xpath('twitter','//a[contains(text(), "twitter")]/@href')
        l.add_xpath('facebook','//a[contains(text(), "facebook")]/@href')
        
                
        return l.load_item()
    
    
    
                         
    