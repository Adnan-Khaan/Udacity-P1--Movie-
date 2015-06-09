import webbrowser


class Movie():
    '''
    This class contains all the attibutes that are 
    required to save information about a movie.
    '''

    def __init__(
        self,
        movie_title,
        movie_storyline,
        poster_image,
        trailer_youtube,
        rating,
        actors,
        release,
                  ):
        '''
        This is the definition of the contructor of class Movie, which
        will be called whenever an object is being created.
        '''    
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = rating
        self.release = release
        self.actors = actors     
    
