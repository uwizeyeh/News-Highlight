class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL =curl https://newsapi.org/v2/top-headlines -G \
    -d country=us \
    -d apiKey=e155a0c2571b47beab68569befc2a877
    pass



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True