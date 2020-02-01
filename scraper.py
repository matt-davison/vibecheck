# Ryan Gniadek
# Scraper Demo
import scrapy


class RedditSpider(scrapy.Spider):
    name = "wsb_spider"

    def start_requests(self):
        urls = [
            'https://old.reddit.com/r/wallstreetbets/search?q=iran&restrict_sr=on'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for header in response.css('header.search-result-header'):
            title = header.css('a.search-title.may-blank').get()
            begin_index = title.find('>')
            end_index = title.find('<', begin_index)
            yield {title[begin_index+1:end_index]}
