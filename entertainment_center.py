# import dependencies
import media
import fresh_tomatoes

interstellar = media.Movie('Interstellar',
                           "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
                            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRCYYPZXEtShEli_JanWrPpuBDRtI8vXiy50OMcFOzYDF3VA3fu",
                            "?v=0vxOhd4qlnA")

europa_report = media.Movie('Europa Report',
                            "An international crew of astronauts undertakes a privately funded mission to search for life on Jupiter's fourth largest moon.",
                            "http://ia.media-imdb.com/images/M/MV5BMjA2OTk5ODkxMl5BMl5BanBnXkFtZTcwODc4MDk0OQ@@._V1_SY317_CR4,0,214,317_AL_.jpg",
                            "?v=XhdRYk1Y8VA")

pulp_fiction = media.Movie('Pulp Fiction',
                           "The lives of two mob hit men, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
                           "http://ia.media-imdb.com/images/M/MV5BMjE0ODk2NjczOV5BMl5BanBnXkFtZTYwNDQ0NDg4._V1_SY317_CR4,0,214,317_AL_.jpg",
                           "?v=ewlwcEBTvcg")

pandoras_promise = media.Movie("Pandora's Promise",
                               "A feature-length documentary about the history and future of nuclear power. The film explores how and why mankind's most feared and controversial technological discovery is now passionately embraced by many of those who once led the charge against it. Operating as history, cultural meditation and contemporary exploration, PANDORA'S PROMISE aims to inspire a serious and realistic debate over what is without question the most important question of our time: how do we continue to power modern civilization without destroying it?",
                               "http://ia.media-imdb.com/images/M/MV5BMTgyNDYxMzQxM15BMl5BanBnXkFtZTcwODQ0NTY0OQ@@._V1_SY317_CR0,0,214,317_AL_.jpg",
                               "?v=bDw3ET3zqxk")

inglourious_basterds = media.Movie("Inglourious Basterds",
                                  "In Nazi-occupied France during World War II, a plan to assassinate Nazi leaders by a group of Jewish U.S. soldiers coincides with a theatre owner's vengeful plans for the same.",
                                  "http://ia.media-imdb.com/images/M/MV5BMjIzMDI4MTUzOV5BMl5BanBnXkFtZTcwNDY3NjA3Mg@@._V1_SY317_CR0,0,214,317_AL_.jpg",
                                  "?v=6AtLlVNsuAc")

shaun_of_the_dead = media.Movie("Shaun of the Dead",
                                "A man decides to turn his moribund life around by winning back his ex-girlfriend, reconciling his relationship with his mother, and dealing with an entire community that has returned from the dead to eat the living.",
                                "http://ia.media-imdb.com/images/M/MV5BMTU2NjA0NDk0NV5BMl5BanBnXkFtZTcwOTA0OTQzMw@@._V1_SX214_AL_.jpg",
                                "?v=yfDUv3ZjH2k")

twenty_eight_days_later = media.Movie("28 Days Later",
                                      "Four weeks after a mysterious, incurable virus spreads throughout the UK, a handful of survivors try to find sanctuary.",
                                      "http://ia.media-imdb.com/images/M/MV5BNzM2NDYwNjM3OF5BMl5BanBnXkFtZTYwNDYxNzk5._V1_SX214_AL_.jpg",
                                      "?v=HEkJAaGhJhQ")

american_ganster = media.Movie("American Gangster",
                               "In 1970s America, a detective works to bring down the drug empire of Frank Lucas, a heroin kingpin from Manhattan, who is smuggling the drug into the country from the Far East.",
                               "http://ia.media-imdb.com/images/M/MV5BMTkyNzY5MDA5MV5BMl5BanBnXkFtZTcwMjg4MzI3MQ@@._V1_SY317_CR5,0,214,317_AL_.jpg",
                               "www.youtube.com/watch?v=BV_nssS6Zkg")

movie_list=[interstellar, europa_report, pulp_fiction, pandoras_promise, inglourious_basterds, shaun_of_the_dead, twenty_eight_days_later, american_ganster]

fresh_tomatoes.open_movies_page(movie_list)