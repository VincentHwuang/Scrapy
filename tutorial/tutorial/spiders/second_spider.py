# -*- coding: utf-8 -*-
import scrapy


class SecondQuotesSpider(scrapy.Spider):
	name = 'second_spider'
#    allowed_domains = ['http://quotes.toscrape.com/page/1']
#    start_urls = ['http://quotes.toscrape.com/page/1/']
	def start_requests(self):
		urls=[
		'http://quotes.toscrape.com/page/1',
		'http://quotes.toscrape.com/page/2'
		]
		for url in urls:
			yield scrapy.Request(url=url,callback=self.parse)

    	def parse(self, response):
		for quote in response.css('div.quote'):
			yield {
			'text'  :  quote.css('span.text::text').extract_first(),
			'author':  quote.css('small.author::text').extract_first(),
			'tags'  :  quote.css('div.tags a.tag::text').extract(),
			}
