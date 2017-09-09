#-*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html


from scrapy.item import Item, Field



class ParlamentItem(Item):
    ime = Field()
    prezime = Field()
    stranka = Field()
    posl_grupa = Field()
    mesto = Field()
    zanimanje = Field()
    godina = Field()
    foto = Field()
    twitter = Field()
    facebook = Field()
    