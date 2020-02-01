from twython import Twython
APP_KEY = 'zI15R3JccQKrtPR1l9siC4K9q'
APP_SECRET = 'lQQCH7ZLusQqJC8QSk3CG5DS7tTzWHHjgkpdasd0he3a4JTBLe'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()
twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
twitter.search(q='python', result_type='popular')
print (twitter.search(q='python', result_type='popular'))
#query = {'q': 'learn python',
 #       'result_type': 'popular',
  #      'count': 10,
   #     'lang': 'en',
    #    }
#python_tweets.search(query='python', result_type='popular')urned a 401 (Unauthorized), Could not authenticate you.