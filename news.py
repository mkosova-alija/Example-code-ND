
from newsdataapi import NewsDataApiClient


# API key authorization, Initialize the client with your API key
api = NewsDataApiClient(apikey='pub_30503bd51e9cacdfa6a40fa77f953a582632c')


# News API
response = api.news_api(q= "corona" , country = "us")
print(response)
