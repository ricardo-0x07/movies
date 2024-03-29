import webbrowser

# Movie class to be used to create instance of various movies


class Movie():

    def __init__(self, title, storyline,
                 poster_image, trailer_youtube):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    # Method to open youtube trailer.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
