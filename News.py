import concurrent.futures
from newsapi import NewsApiClient

def newsQuery(query):
    def getNews():
        api = NewsApiClient(api_key='b13dacd3cd0d475b80da08eec5fafb13')
        all_headlines = ""
        for pageNum in range(1,6):
            all_articles = api.get_everything(q=query, page=pageNum).get('articles')

            for article in all_articles:
                headline = article.get('title')
                if (headline is not None):
                    all_headlines = all_headlines+headline

        return all_headlines

    '''
    with concurrent.futures.ThreadPoolExecutor() as executor:
        #code to start each scrape as a thread
        news = executor.submit(getNews())
        #end add thread

        #add results to return string
    '''
    ret = list()
    ret.append(getNews())
    return ret