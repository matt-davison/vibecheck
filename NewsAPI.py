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

print(GetNews('China'))