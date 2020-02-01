from newsapi import NewsApiClient

api = NewsApiClient(api_key='64c70df4109b49529da4fa0dbbf949e1')

print(api.get_everything(q='Iran').get('title'))

