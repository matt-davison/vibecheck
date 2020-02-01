# Ryan Gniadek
# Scraper Demo
import scrapy
from scrapy.http import TextResponse


class RedditSpider(scrapy.Spider):
    def __init__(self, query):
        self.name = 'wsb_spider'
        self.query = query
        base_url = 'https://old.reddit.com/r/all/search?q='
        self.response = TextResponse(url=base_url+query, encoding = 'utf-8')

    def start_requests(self):
        search_url = 'https://old.reddit.com/r/all/search?q='

        urls = [
            search_url+self.query
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for header in response.css('header.search-result-header'):
            title = response.css('a.search-title.may-blank').get()
            begin_index = title.find('>')
            end_index = title.find('<', begin_index)
            yield {title[begin_index+1:end_index]}
