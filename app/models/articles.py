class Article:
    '''
    Class that instantiates objects of the news article objects of the news sources
    '''
    def __init__(self,author,description,time,url,image,title):

        self.author = author
        self.description = description
        self.time = time
        self.url = url
        self.image = image
        self.title = title
