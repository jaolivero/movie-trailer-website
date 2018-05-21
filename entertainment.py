import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that", "https://images-na.ssl-images-amazon.com/images/I/91g2fEXursL._RI_SX200_.jpg", "https://www.youtube.com/watch?v=4KPTXpQehio ")
dark_knight = media.Movie("Dark Knight", "Batman goes up against joker", "https://i.ytimg.com/vi/qY3UkAHufLY/movieposter.jpg", "https://www.youtube.com/watch?v=EXeTwQWrcwY")
forrest_gump = media.Movie("Forrest Gump", "A boys adventure into adulthood", "https://img.etsystatic.com/il/cbafe5/1303342253/il_fullxfull.1303342253_qphh.jpg?version=0", "https://www.youtube.com/watch?v=bLvqoHBptjg")
lion_king = media.Movie("Lion King","A lion must reclaim his kingdom","https://images-na.ssl-images-amazon.com/images/I/51Q0R48W6PL._SX335_BO1,204,203,200_.jpg", "https://www.youtube.com/watch?v=4sj1MT05lAA")
hunger_games = media.Movie("Hunger Games", "Young girl must fight until death to survive", "https://s.yimg.com/fz/api/res/1.2/IwKKM9DrzSodB5xs48VTig--~C/YXBwaWQ9c3JjaGRkO2ZpPWZpbGw7aD0yMDQ7cHhvZmY9MDtweW9mZj0wO3E9ODA7dz0xMzc-/http://d1.yimg.com/sr/imgv1/4/53e91743-7090-3876-90f3-b09e2eafba4b", "https://www.youtube.com/watch?v=FovFG3N_RSU" )
a_bronx_tale = media.Movie("A Bronx Tale", "The mafias influence on a boy", "https://images-na.ssl-images-amazon.com/images/I/91BdILZCvYL._RI_SX200_.jpg", "https://www.youtube.com/watch?v=z50PjmZYS4A")

movies = [toy_story, dark_knight, forrest_gump, lion_king, hunger_games, a_bronx_tale]
fresh_tomatoes.open_movies_page(movies)
