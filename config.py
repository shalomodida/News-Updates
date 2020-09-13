import os
class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?language=en&apiKey='
    ARTICLES_API_BASE_URL ='http://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
   
class ProdConfig(Config):
    pass

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General
        configuration settings. We have added the debug= true which
        enables debug mode in our application.
    '''
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}




