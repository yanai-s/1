import scrapy
from scrapy.linkextractors import LinkExtractor

class getyahoo(scrapy.Spider):
    name = "tvkingdom"
    allowed_domains = ["tv.so-net.ne.jp"]
    start_urls = (
        'http://tv.so-net.ne.jp/schedulesBySearch.action?condition.genres[0].parentId=106000&condition.genres[0].childId=-1&stationPlatformId=0&condition.keyword=&submit=&index=0',
    )
    rules = [LinkExtractor(allow=r'/schedulesBySearch.action?condition.genres[0].parentId=106000&condition.genres[0].childId=-1&stationPlatformId=0&condition.keyword=&submit=&index=\d/')
    ]

    def parse(self, response):
        for tvkingdom in response.css('div.utileList'):
            yield {
                'title': tvkingdom.css('h2 a::text').extract_first(),
                'day': tvkingdom.css('p::text').extract_first(),
            }
