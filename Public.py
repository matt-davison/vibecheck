import concurrent.futures
from reddit import RedditSpider


def pubQuery(query):
    redditScraper = RedditSpider(query)

    def scrapeReddit():
        redditScraper.parse(redditScraper.search_url)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # code to start each scrape as a thread
        reddit = executor.submit(scrapeReddit)
        # end add thread

        # add results to return string
        ret = []
        ret.append(reddit.result())

        return ret
