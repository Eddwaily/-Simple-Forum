import webbrowser
class Movie() :
    def __init__( self, title, storyline, poster_image, youtube_trailer) :
        self.title = title
        storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer
    def _show_trailer(self) :
        webbrowser.open(self.trailer_youtube_url)
