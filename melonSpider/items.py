# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class songItem(scrapy.Item):
    artist = scrapy.Field()
    song = scrapy.Field()
    artistID = scrapy.Field()
    withArtist = scrapy.Field()
    withID = scrapy.Field()
    
