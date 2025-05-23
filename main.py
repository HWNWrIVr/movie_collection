from movie import Movie
from collection import MovieCollection

def main():
    my_collection = MovieCollection()
    
    movies_to_add = [
        Movie("Крестный отец", 1972, "Фрэнсис Форд Коппола", "Криминал", 9.2),
        Movie("Форрест Гамп", 1994, "Роберт Земекис", "Драма", 8.8),
    ]
    
    for movie in movies_to_add:
        my_collection.add_movie(movie)
    
    print("Вся коллекция:")
    for movie in my_collection:
        print(movie)
    
    print("\n Криминальные фильмы:")
    for movie in my_collection.search_by_genre("криминал"):
        print(movie)

if __name__ == "__main__":
    main() 