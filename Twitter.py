from twython import Twython
import datetime
def GetTweets(searchTerm):
    APP_KEY = 'zI15R3JccQKrtPR1l9siC4K9q'
    APP_SECRET = 'lQQCH7ZLusQqJC8QSk3CG5DS7tTzWHHjgkpdasd0he3a4JTBLe'
    twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
    ACCESS_TOKEN = twitter.obtain_access_token()
    twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
    query=searchTerm
    searchResults = []
    tweetTextList = []
    for x in range (0, 14):
        searchResults.append(twitter.search(q=query, result_type='popular', until=str(datetime.date.today()-datetime.timedelta(x))))
    for x in range(0, len(searchResults)):
        for y in range(0, len(searchResults[x].get('statuses'))):
            initialText = searchResults[x].get('statuses')[y].get('text')
            endIndex = initialText.find("https")
            linklessText = initialText[0:endIndex]
            tweetTextList.append(linklessText)
    return tweetTextList


print(GetTweets('iran'))



