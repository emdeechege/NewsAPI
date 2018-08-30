from app import app
import urllib.request,json
# from .models import sources
from .models import sources

Source = sources.Source

#API key
api_key = app.config['NEWS_API_KEY']
#source url
source_url= app.config['NEWS_API_SOURCE_URL']

def get_source():
    '''
    Function that gets the json response to url request
    '''
    get_source_url= source_url.format(api_key)
    with urllib.request.urlopen(get_source_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)

    return source_results

def process_results(source_list):
    '''
    function to process results and transform them to a list of objects
    Args:
        source_list:dictionary cotaining source details
    Returns:
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        if id:
            source_object = Source(id,name,description,url)
            source_results.append(source_object)

    return source_results

def article_source(id):
    article_source_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={'.format(id,api_key)
    with urllib.request.urlopen(article_source_url) as url:
        article_source_data = url.read()
        article_source_response = json.loads(article_source_data)

        article_source_results = None

        if article_source_response['articles']:
            article_source_list = article_source_response['articles']
            article_source_results = process_results(article_source_list)


    return article_source_results

def process_articles(articles_response):
    '''
    function that processes the json files of articles from the api key
    '''
    my_articles_list = []
    for article in articles_response:
        article_name = article.get('author')
        article_description = article.get('description')
        article_time = article.get('publishedAt')
        article_image = article.get('urlToImage')
        article_url = article.get('url')
        article_title = article.get ('title')
        article_objects = News_Highlights_by_source(article_name,article_description,article_time,article_image,article_url, article_title)
        my_articles_list.append(article_objects)

    return my_articles_list
