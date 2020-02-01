
from twython import Twython
import datetime
import praw

import concurrent.futures


def pubQuery(query):
    def SearchReddit():
        reddit = praw.Reddit(client_id='a0MDpc36OCJQXg', client_secret='uVYddWR6gzHHI_KrwXy2AlqrdXo',
                            user_agent='Vibe Check')

        search = reddit.subreddit('all').search(query=query, sort='top', time_filter='week')

        all_titles = ""

        for submission in search:
            if (submission is not None):
                all_titles = all_titles + submission.title

        return all_titles

    def getTweets():
        dank = 'zI15R3JccQKrtPR1l9siC4K9q'
        meme = 'lQQCH7ZLusQqJC8QSk3CG5DS7tTzWHHjgkpdasd0he3a4JTBLe'
        twitter = Twython(dank, meme, oauth_version=2)
        ACCESS_TOKEN = twitter.obtain_access_token()
        twitter = Twython(dank, access_token=ACCESS_TOKEN)
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
