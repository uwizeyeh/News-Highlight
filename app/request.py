from app import app
import urllib.request,json
from .models import source
from .models import news
Source = source.Source
News = news.News

# getting api key
api_key = app.config['NEWS_API_KEY']
# getting the news base url

base_url = app.config['SOURCE_API_BASE_URL']
articles_base_url=app.config['NEWS_API_BASE_URL']

def get_source(category):
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = base_url.format(category,api_key)
    print(get_source_url)
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)
        source_results = get_source_response
        if get_source_response['sources']:
           
            source_results_list = get_source_response['sources']
            source_results = process_result(source_results_list)
    return source_results
def process_result(source_list):
    '''
    Function that processes the news result and transform them to a list of objects
    
    Args:
       new_list: A list of dictionaries that contain news details
    Returns:
       news_results:A list of objects
    '''
    source_results =[]
    for source_item in source_list:
       
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        if source:
            source_object = Source(id,name,description)
            source_results.append(source_object)
    return source_results

def get_news(id):
    get_news_details_url = articles_base_url.format(id,api_key)
    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)
        news_object = None
        
        if news_details_response['articles']:
                news_results_list=news_details_response['articles']
                news_results=process_news(news_results_list)
    return news_results
def process_news(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects
    Args:
    newz_list: A list of dictionaries that contain news details
    Returns :
    news_results: A list of articles objects
    '''
    news_results=[]
    for article in news_list:
        author=article.get('author')
        title=article.get('title')
        description=article.get('description')
        url=article.get('url')
        imageUrl=article.get('urlToImage')
        publishedAt=article.get("publishedAt")
        content=article.get('content')

        if imageUrl:
            article_object=News(author,title,description,url,imageUrl,publishedAt,content)
            news_results.append(article_object)
    return news_results 
