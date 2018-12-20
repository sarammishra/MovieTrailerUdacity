# TASK: Define a movie class

import webbrowser


# Store movie info within this class

class movie():
    """This class creates CHARS required for all movies
        Attributes:
        attr1 (str): title of movie.
        attr2 (str): Quick Summary of Movie
        attr3 (hyperlink): Poster Link to creative commons image 
        attr4 (hyperlink): Trailer Link to youtube Trailer
        
        """
    
    def __init__(self, movieTitle, movieStory, poster, trailer):
        self.title = movieTitle
        self.story = movieStory
        self.poster = poster
        self.trailer = trailer

    def display_trailer(self):
        webbrowser.open(self.trailer)
