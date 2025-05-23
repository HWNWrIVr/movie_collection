from typing import Dict, List, Optional
from movie import Movie
from iterator import MovieIterator

class MovieCollection:
    def __init__(self):
        self._movies: Dict[str, Movie] = {}
        self._collections: Dict[str, Dict[str, Movie]] = {}

    def add_movie(self, movie: Movie, collection_name: Optional[str] = None) -> bool:
        if movie.title in self._movies:
            return False
        self._movies[movie.title] = movie
        if collection_name:
            if collection_name not in self._collections:
                self._collections[collection_name] = {}
            self._collections[collection_name][movie.title] = movie
        return True

    def remove_movie(self, title: str) -> bool:
        removed = self._movies.pop(title, None) is not None
        if removed:
            for collection in self._collections.values():
                collection.pop(title, None)
        return removed

    def add_movie_to_collection(self, collection_name: str, movie_title: str) -> bool:
        if movie_title not in self._movies:
            return False
        if collection_name not in self._collections:
            self._collections[collection_name] = {}
        self._collections[collection_name][movie_title] = self._movies[movie_title]
        return True

    def remove_movie_from_collection(self, collection_name: str, movie_title: str) -> bool:
        if collection_name in self._collections and movie_title in self._collections[collection_name]:
            del self._collections[collection_name][movie_title]
            return True
        return False

    def search_by_genre(self, genre: str) -> List[Movie]:
        return [m for m in self._movies.values() if m.genre.lower() == genre.lower()]

    def search_movie(
        self,
        title: Optional[str] = None,
        genre: Optional[str] = None,
        year: Optional[int] = None
    ) -> List[Movie]:
        results = []
        for movie in self._movies.values():
            if title and title.lower() not in movie.title.lower():
                continue
            if genre and genre.lower() != movie.genre.lower():
                continue
            if year and year != movie.year:
                continue
            results.append(movie)
        return results

    def get_movies_from_collection(self, collection_name: str) -> List[Movie]:
        if collection_name in self._collections:
            return list(self._collections[collection_name].values())
        return []

    def __iter__(self):
        return MovieIterator(self._movies)
