from typing import Dict, List
from movie import Movie
from iterator import MovieIterator

class MovieCollection:
    def __init__(self):
        self._movies: Dict[str, Movie] = {}
        
    def add_movie(self, movie: Movie) -> bool:
        if movie.title in self._movies:
            return False
        self._movies[movie.title] = movie
        return True
        
    def remove_movie(self, title: str) -> bool:
        return self._movies.pop(title, None) is not None
        
    def search_by_genre(self, genre: str) -> List[Movie]:
        return [m for m in self._movies.values() if m.genre.lower() == genre.lower()]
        
    def __iter__(self):
        return MovieIterator(self._movies)