# Ryan Gniadek
# Scraper Demo
import scrapy


class RedditSpider(scrapy.Spider):
    name = "wsb_spider"

    def start_requests(self):
        urls = [
            'https://www.reddit.com/r/wallstreetbets/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = "quotes-%s.html" % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
