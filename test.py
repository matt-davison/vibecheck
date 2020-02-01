from reddit import RedditSpider

redditScraper = RedditSpider("Iran")


next(redditScraper.parse(response=redditScraper.response))


