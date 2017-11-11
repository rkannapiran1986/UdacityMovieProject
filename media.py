import webbrowser

class Video():
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

class Movie(Video):
    """Document for Movie class"""
    def __init__(self, movie_title, movie_storyline, poster_img, trailer_youtube, duration):
        #mDetail = Video.__init__(self, movie_title, duration)
        """Calling Video Call to get Title and duration"""
        mDetail = Video(movie_title, duration)
        self.title = mDetail.title
        self.storyline = movie_storyline
        self.poster_image_url = poster_img
        self.trailer_youtube_url = trailer_youtube
        self.duration = mDetail.duration

    def showTrailer(self):
        webbrowser.open(self.trailer_url)

class TvShow(Video):
    """Document for TvShow class"""
    def __init__(self, season_title, season, episode, tv_station, duration):
        #mDetail = Video.__init__(self, season_title, duration)
        """Calling Video Call to get Title and duration"""
        mDetail = Video(season_title, duration)
        self.title = mDetail.title
        self.storyline = season
        self.episode = episode
        self.tv_station = tv_station
        self.poster_image_url = episode
        self.trailer_youtube_url = tv_station
        self.duration = mDetail.duration
