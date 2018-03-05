import fresh_tomatoes
from media import Movie

toy_story = Movie("Toy Story", "A kid toys comes to life","https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = Movie("Avatar", "some sort of wierd thing","https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

need_for_speed = Movie("Need for speed", "a street racer who was framed by a wealthy business associate joins a cross country race with revenge in mind.","https://upload.wikimedia.org/wikipedia/en/e/e3/Need_For_Speed_poster.jpg", "https://www.youtube.com/watch?v=u3wtVI-aJuw")

ride_along = Movie("Ride Along", "The best comedy movie 2012","https://upload.wikimedia.org/wikipedia/en/d/d8/Ride_Along_poster.jpg", "https://www.youtube.com/watch?v=5klp6rkHIks")

interstellar = Movie("interstellar", "Award winning 2014 sci-fi movie","https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg", "https://www.youtube.com/watch?v=ePbKGoIGAXY")

zootopia = Movie("Zootopia", "animation movie about a rabbit that dreams to be a cup in the world of animals","https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg", "https://www.youtube.com/watch?v=jWM0ct-OLsM")

movies = [toy_story, avatar, need_for_speed, ride_along, interstellar, zootopia]
#magic variables for Movies class
print "Namespaces: " + Movie.__name__
print "Name: " + Movie.__name__
print "Module: " + Movie.__module__
print "Documentation:/n" + Movie.__doc__

fresh_tomatoes.open_movies_page( movies )
