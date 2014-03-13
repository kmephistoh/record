from scrapy.spider import BaseSpider
from scrapy.selector  import Selector


class HnSpider(BaseSpider):
	name = 'hn'
	allowed_domains = []
	start_urls = ['http://news.ycombinator.com']

	def parse(self, response):
		sel = Selector(response)
		site = sel.xpath('//td[@class="title"]')
		for site in sites:
			title =site.xpath('a/text()').extract()
			link = site.xpath('a/@href').extract()
			print title, link