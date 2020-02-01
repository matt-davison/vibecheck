import concurrent.futures
from newsapi import NewsApiClient

def finQuery(query):
    def getFinancial():
        api = NewsApiClient(api_key='64c70df4109b49529da4fa0dbbf949e1')
        all_headlines = ''
        for pageNum in range(1,6):
            all_articles = api.get_everything(q=query, page=pageNum).get('articles')

            for article in all_articles:
                headline = article.get('title')
                all_headlines = all_headlines+headline

        return all_headlines
    '''
    with concurrent.futures.ThreadPoolExecutor() as executor:
        #code to start each scrape as a thread
        bloomberg = executor.submit(scrapeBloomberg)
        #end add thread

        #add results to return string
        ret = list()
        ret.append(bloomberg.result())
    '''
    ret = list()
    ret.append(getFinancial())
    return ret
    