from typing import Dict, List, Optional, Iterator


class Movie:
    def __init__(self, title: str, genre: str, year: int):
        self.title = title
        self.genre = genre
        self.year = year

    def __str__(self) -> str:
        return f"{self.title} ({self.year}) - {self.genre}"


class MovieIterator:
    def __init__(self, movies: Dict[str, "Movie"]):
        self._movies = list(movies.values())
        self._index = 0

    def __iter__(self) -> "MovieIterator":
        return self

    def __next__(self) -> Movie:
        if self._index < len(self._movies):
            movie = self._movies[self._index]
            self._index += 1
            return movie
        raise StopIteration


class MovieCollection:
    def __init__(self):
        self.movies: Dict[str, Movie] = {}

    def add_movie(self, movie: Movie) -> None:
        self.movies[movie.title] = movie

    def remove_movie(self, title: str) -> None:
        if title in self.movies:
            del self.movies[title]

    def __iter__(self) -> Iterator[Movie]:
        return MovieIterator(self.movies)

    def search_movie(
        self,
        title: Optional[str] = None,
        genre: Optional[str] = None,
        year: Optional[int] = None
    ) -> List[Movie]:
        results = []
        for movie in self.movies.values():
            if title and title.lower() not in movie.title.lower():
                continue
            if genre and genre.lower() != movie.genre.lower():
                continue
            if year and year != movie.year:
                continue
            results.append(movie)
        return results
