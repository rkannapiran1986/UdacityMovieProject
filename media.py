import webbrowser


class Video():
    """ this is commonly shared class """
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration


class Movie(Video):
    """Document for Movie class.

        This will have entire details about Movie
    """
    def __init__(self, movie_title, sline, p_img, t_youtube, duration):
        """ Calling Video Call to get Title and duration """
        mDetail = Video(movie_title, duration)
        self.title = mDetail.title
        self.storyline = sline
        self.poster_image_url = p_img
        self.trailer_youtube_url = t_youtube
        self.duration = mDetail.duration

    def showTrailer(self):
        """ Function for calling show trailer (single movie) """
        webbrowser.open(self.trailer_url)


class TvShow(Video):
    """Document for TvShow class.

        This will have entire details about TV serials
    """
    def __init__(self, season_title, season, episode, tv_station, duration):
        """Calling Video Call to get Title and duration"""
        mDetail = Video(season_title, duration)
        self.title = mDetail.title
        self.storyline = season
        self.episode = episode
        self.tv_station = tv_station
        self.poster_image_url = episode
        self.trailer_youtube_url = tv_station
        self.duration = mDetail.duration
