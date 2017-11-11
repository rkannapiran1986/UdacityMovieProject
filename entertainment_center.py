import media
import fresh_tomatoes


# Here is the list of movies describe the instance of Movie and TvShow Classes
avatar = media.Movie('Avatar',
                     'new movie',
                     'https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg',
                     'https://www.youtube.com/watch?v=5PSNL1qE6VY',
                     '2h 42m')

ironMan = media.Movie('Iron Man 3',
                      'new movie for iron man',
                      'http://www.swiftfilm.com/wp-content/uploads/2013/01/IRON3_BusShelter_Falling_v7.jpg',
                      'https://www.youtube.com/watch?v=Ke1Y3P9D0Bc',
                      '2h 10m')

antMan = media.Movie('Ant-Man',
                     'Man becoming a super hero',
                     'https://pre11.deviantart.net/205c/th/pre/i/2015/129/9/d/ant_man_poster_by_gingerjmez-d8spj3h.jpg',
                     'https://www.youtube.com/watch?v=pWdKf3MneyI',
                     '1h 58m')

spiderMan = media.Movie('Spider Man',
                        'Man who do super duper stunts..',
                        'https://lumiere-a.akamaihd.net/v1/images/image_ccc4b657.jpeg',
                        'https://www.youtube.com/watch?v=rk-dF1lIbIg',
                        '2h 13m')

threeIdiots = media.Movie('3 Idiots',
                          'Indian Movie about three friends',
                          'https://sc-events.s3.amazonaws.com/4224477/main.jpg',
                          'https://www.youtube.com/watch?v=xvszmNXdM4w',
                          '2h 51m')

big_bang_theory = media.TvShow('The Big Bang Theory',
                               'Season 10',
                               'http://www.gstatic.com/tv/thumb/tvbanners/14215412/p14215412_b_v8_ad.jpg',
                               'https://www.youtube.com/watch?v=WBb3fojgW0Q',
                               'September 19, 2016 - May 11, 2017')

movies = [avatar,
          ironMan,
          antMan,
          spiderMan,
          threeIdiots,
          big_bang_theory]


fresh_tomatoes.open_movies_page(movies)
