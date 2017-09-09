# -*- coding: utf-8 -*-
import scrapy


class LinkItem(scrapy.Item):
      links = scrapy.Field()

class SkupSpider(scrapy.Spider):
    name = 'skup'
    allowed_domains = ['http://www.parlament.rs']
    start_urls = ['http://www.parlament.gov.rs/narodna-skupstina-/sastav/narodni-poslanici/aktuelni-saziv.890.html']

    def parse(self, response):
        selector = response.xpath('//strong//a/@href') 
        items =[]
        for url in selector.extract():
            items.append(LinkItem(links = 'http://www.parlament.rs' + url))
        return items
    
    
    
    
    
    
            
