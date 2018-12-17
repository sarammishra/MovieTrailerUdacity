#TASK: Define a modie class
import webbrowser

## Store movie info within this class

class movie:
    def __init__(self,movieTitle, movieStory, poster, trailer):
        self.title = movieTitle
        self.story = movieStory
        self.poster = poster
        self.trailer = trailer

    def display_trailer(self):
        webbrowser.open(self.trailer)
