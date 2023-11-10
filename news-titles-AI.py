from newsdataapi import NewsDataApiClient

# API key authorization, Initialize the client with your API key
api = NewsDataApiClient(apikey='pub_30503bd51e9cacdfa6a40fa77f953a582632c')

# News API
response = api.news_api(qInTitle="Artificial&Intelligence", country="us")

# Check if the request was successful
if response['status'] == 'success':
    # Iterate through the list of articles and print titles
    for article in response['results']:
        print(article['title'])
else:
    print("Error in API request:", response['message'])
