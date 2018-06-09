import media
import fresh_tomatoes
#Above I imported th files 'media' and 'fresh_tomatoes' to use the predefined classes in this code.
#Below are the movies I turned into instances using the 'media' file and 'Movie class'.
#Each instance below gives the following info: the_movie = media.Movie(title, storyline, poster, trailer)
toy_story = media.Movie("Toy Story", "A story of a boy and his toys come to life", "http://cdn.collider.com/wp-content/uploads/toy-story-poster1.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", "A marine on an alien planet", "https://sleephotography.files.wordpress.com/2013/05/avatar_poster_21.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")

paid_in_full = media.Movie("Paid in Full", "A Harlem crime story", "https://www.movieposter.com/posters/archive/main/105/MPW-52923", "https://www.youtube.com/watch?v=Y63NfERYsL4")

juice = media.Movie("Juice", "A tale of four Harlem friends and betrayel", "https://www.movieposter.com/posters/archive/main/32/MPW-16164", "https://www.youtube.com/watch?v=ECi021J_j18")

world_war_z = media.Movie("World War Z", "A fictional tale of a zombie apocalypse", "http://www.shockya.com/news/wp-content/uploads/World-War-Z-Final-Movie-Poster.jpg", "https://www.youtube.com/watch?v=slfrrjPndV4")

slowm = media.Movie("The Secret Life of Walter Mitty", "A story of a man making his daydreams a reality", "https://m.media-amazon.com/images/M/MV5BODYwNDYxNDk1Nl5BMl5BanBnXkFtZTgwOTAwMTk2MDE@._V1_UX182_CR0,0,182,268_AL_.jpg", "https://www.youtube.com/watch?v=HddkucqSzSM")
#The list below gathers all the instances so we can have the ability to pass them through the fresh_tomatoes.open_movies_page() function.
movies = [toy_story, avatar, paid_in_full, juice, world_war_z, slowm]

fresh_tomatoes.open_movies_page(movies)
