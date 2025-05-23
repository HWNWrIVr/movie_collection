from typing import Iterator, Dict
from movie import Movie

class MovieIterator(Iterator[Movie]):
    def __init__(self, movies: Dict[str, Movie]):
        self._movies = list(movies.values())
        self._index = 0
        
    def __next__(self):
        if self._index < len(self._movies):
            result = self._movies[self._index]
            self._index += 1
            return result
        raise StopIteration