
from newsdataapi import NewsDataApiClient


# API key authorization, Initialize the client with your API key
api = NewsDataApiClient(apikey='pub_*********')


# News API
response = api.news_api(q= "corona" , country = "us")
print(response)
