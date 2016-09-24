import media
import fresh_tomatoes
batman_begins = media.Movie("Batman Begins",
                        "The dark knights origin story retold.",
                        "http://trailers.apple.com/trailers/wb/batman_begins/trailer4/images/index_03.jpg",
                        "https://www.youtube.com/watch?v=neY2xVmOfUM")

#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an Alien Planet",
                     "http://orig15.deviantart.net/a0e7/f/2010/192/b/e/avatar_special_edition_poster_by_j_k_k_s.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")

#print(avatar.storyline)
#avatar.show_trailer()

avengers = media.Movie("Avengers Age of Ultron",
                     "A self aware AI tries to save the world, by rendering humanity extinct.",
                     "http://cdn.collider.com/wp-content/uploads/avengers-age-of-ultron-poster1.jpg",
                     "https://www.youtube.com/watch?v=JAUoeqvedMo")

#print(avengers.storyline)
#avengers.show_trailer()

django_unchained  = media.Movie("Django Unchained ",
                     "Bounty hunting slave, searching for his hot wife.",
                     "http://www.newdvdreleasedates.com/images/posters/large/django-unchained-2012-05.jpg",
                     "https://www.youtube.com/watch?v=2h9MRdO6eyE")

divergent = media.Movie("Divergent",
                     "A girl is determine to not be defined by what society expects of her",
                     "http://i2.wp.com/www.heyuguys.com/images/2014/03/Divergent-UK-Poster.jpg",
                     "https://www.youtube.com/watch?v=sutgWjz10sM")

man_of_steel = media.Movie("Man of Steel",
                     "A story about living on purpose",
                     "http://img15.deviantart.net/7936/i/2015/111/a/0/man_of_steel_poster_2_by_jonesyd1129-d6f6321.jpg",
                     "https://www.youtube.com/watch?v=T6DJcgm3wNY")

hunger_games = media.Movie("Hunger Games",
                     "A really real reality show",
                     "https://flashbackbackslide.files.wordpress.com/2014/02/catching-fire-movie-poster.jpg",
                     "https://www.youtube.com/watch?v=PbA63a7H0bo")

movies = [batman_begins, avatar, avengers, django_unchained, divergent, man_of_steel, hunger_games]

#fresh_tomatoes.open_movies_page(movies)
