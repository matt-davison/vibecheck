
from twython import Twython
import datetime
import praw
import concurrent.futures
from Keys import getKey

def pubQuery(query):
    def SearchReddit():
        id = getKey("RedditAPI", "id")
        secret = getKey("RedditAPI", "secret")
        reddit = praw.Reddit(client_id=id, client_secret=secret,
                            user_agent='Vibe Check')

        search = reddit.subreddit('all').search(query=query, sort='top', time_filter='week')

        all_titles = ""

        for submission in search:
            if (submission is not None):
                all_titles = all_titles + submission.title

        return all_titles

    def getTweets():
        key = getKey("TwitterAPI", "key")
        secret = getKey("TwitterAPI", "secret")
        twitter = Twython(key, secret, oauth_version=2)
        ACCESS_TOKEN = twitter.obtain_access_token()
        twitter = Twython(key, access_token=ACCESS_TOKEN)
        searchResults = []
        tweetTextList = []
        for x in range(0, 14):
            searchResults.append(twitter.search(lang='en', q=query, result_type='popular', until=str(
                datetime.date.today()-datetime.timedelta(x))))
        for x in range(0, len(searchResults)):
            for y in range(0, len(searchResults[x].get('statuses'))):
                initialText = searchResults[x].get('statuses')[y].get('text')
                endIndex = initialText.find("https")
                linklessText = initialText[0:endIndex]
                tweetTextList.append(linklessText)
        toReturn = ""
        for string in tweetTextList:
            toReturn += str(string)
        return toReturn

    '''
    with concurrent.futures.ThreadPoolExecutor() as executor:
        #code to start each scrape as a thread
        tweets = executor.submit(getTweets())
        #end add thread

        #add results to return string
        ret = list()
        ret.append(tweets.result())

    '''
    ret = list()
    ret.append(getTweets())
    ret.append(SearchReddit())
    return ret
