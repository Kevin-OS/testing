import scrapy

class PriceSpider(scrapy.Spider):
    name = "prices"
    start_urls = ['https://shop.supervalu.ie/shopping/allaisles', ]
    
    def parse(self, response):
        for price in response.css('div.product-list-item-details'):
            yield {
                'Item': price.css('h4.product-list-item-details-title::text').extract_first(),
                'Price': price.css('span.data-unit-price::text').extract_first(),
            }
