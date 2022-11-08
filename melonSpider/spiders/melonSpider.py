import scrapy
from melonSpider.items import songItem
import re

class melonSpider(scrapy.Spider):
    name = "melonSpider"
    start_urls = ["https://www.melon.com/artist/songPaging.htm?&listType=F&artistId=261143"]
    def parse(self, response):
        songitem = songItem()
        songitem['song'] = response.xpath(r'//*[@id="frm"]/div/table/tbody/tr/td[3]/div/div/a/text()').getall()
        songitem['artistID'] = response.url.split('artistId=')
        songitem['withArtist'] = response.xpath(r'//*[@id="artistName"]/a/text()').getall()
        withl = response.xpath(r'//*[@id="frm"]/div/table/tbody/tr/td[4]/div/div/a/@href').getall()
        songitem['withID'] = [re.findall(r"goArtistDetail\(\'(.*?)\'\)", i)[0] for i in withl]
        req_urls = [ r"https://www.melon.com/artist/songPaging.htm?&listType=F&artistId=" + re.findall(r"goArtistDetail\(\'(.*?)\'\)", i)[0] for i in withl]
        yield songitem
        if req_urls:
            for i in req_urls:
                yield scrapy.Request(i, callback=self.parse)