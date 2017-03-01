import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['http://www.met.ie/forecasts/', ]
    
    def parse(self, response):
        for quote in response.css('td.maincontent'):
            yield {
                'when': quote.css('span.daybox::text').extract_first(),
                'forecast': quote.css('p::text').extract_first(),
            }
