# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line
# 1. 
movies = ['steen der wijzen', 'geheime kamer', 'gevangen van askaban', 'vuurbeker', 'order van de feniks', 'halfbloed prins', 'reliek van de dood']

def alphabetical_order(list):
    list.sort()
    list_in_order = list
    return list_in_order

print(alphabetical_order(movies))

# 2. 
def won_golden_globe(did_the_movie_win):
    winning_movies = ['jaws', 'star wars: episode iv - a new hope', 'e.t. the extra-terrestrial', 'memoirs of a geisha']
    did_the_movie_win_lower = did_the_movie_win.lower()
    return did_the_movie_win_lower in winning_movies

print(won_golden_globe('paws'))

# 3.
film_names = ['The Poseidon Adventure', 'Cinderella Liberty', 'Tom Sawyer', 'Earthquake', 'Jaws', 'Close Encounters of the Third Kind', 'Star Wars: Episode IV – A New Hope', 'Superman', 
'Star Wars: Episode V – The Empire Strikes Back', 'E.T. the Extra-Terrestrial', '"If We Were in Love" (from Yes, Giorgio)', 'The River', 'Empire of the Sun', 'The Accidental Tourist', 
'Born on the Fourth of July', 'Schindler\'s List', '"Moonlight" (from Sabrina)', 'Seven Years in Tibet', 'Saving Private Ryan', 'Angela\'s Ashes', 'A.I. Artificial Intelligence', 
'Memoirs of a Geisha', 'War Horse', 'Lincoln', 'The Book Thief', 'The Post']

def remove_toto_albums(albums):
    toto_albums = ['Fahrenheit', 'The Seventh One', 'Toto XX', 'Falling in Between', 
                    '35th Anniversary', 'Live in Poland', 'Toto XIV', 'Old Is New', 
                    '40 Tours Around the Sun', 'With a Little Help from My Friends']
    tidy_list = [song for song in albums if song not in toto_albums]
    return tidy_list

print(remove_toto_albums(film_names))