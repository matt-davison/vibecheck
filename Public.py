
from twython import Twython
import datetime
from newsapi import NewsApiClient

def GetNews(searchTerm):
    api = NewsApiClient(api_key='64c70df4109b49529da4fa0dbbf949e1')

    all_headlines = ''

    for pageNum in range(1,6):
        all_articles = api.get_everything(q=searchTerm, page=pageNum).get('articles')

        for article in all_articles:
            headline = article.get('title')
            all_headlines = all_headlines+headline

    return all_headlines


def GetTweets(searchTerm):
    dank = 'zI15R3JccQKrtPR1l9siC4K9q'
    meme = 'lQQCH7ZLusQqJC8QSk3CG5DS7tTzWHHjgkpdasd0he3a4JTBLe'
    twitter = Twython(dank, meme, oauth_version=2)
    ACCESS_TOKEN = twitter.obtain_access_token()
    twitter = Twython(dank, access_token=ACCESS_TOKEN)
    query=searchTerm
    searchResults = []
    tweetTextList = []
    for x in range (0, 14):
        searchResults.append(twitter.search(lang='en', q=query, result_type='popular', until=str(datetime.date.today()-datetime.timedelta(x))))
    for x in range(0, len(searchResults)):
        for y in range(0, len(searchResults[x].get('statuses'))):
            initialText = searchResults[x].get('statuses')[y].get('text')
            endIndex = initialText.find("https")
            linklessText = initialText[0:endIndex]
            tweetTextList.append(linklessText)
    toReturn = ""
    for string in tweetTextList:
        toReturn+=str(string)
    return toReturn

import concurrent.futures

def pubQuery(query):
    def scrapeReddit():
        print("todo")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        #code to start each scrape as a thread
        reddit = executor.submit(scrapeReddit)
        #end add thread

        #add results to return string
        ret = []
        ret.append(reddit.result())


        return ret

