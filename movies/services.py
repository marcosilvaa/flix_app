from movies.repository import MovieRepository


class MovieService:
    
    
    def __init__(self):
        self.movie_repository = MovieRepository()
    
    
    def get_movies(self):
        return self.movie_repository.get_movies()
    
    
    def create_movie(self, title, genre, actors, release_date, resume):
        movie = dict(
            title=title,
            genre=genre,
            actors=actors,
            release_date=release_date,
            resume=resume,
        )
        return self.movie_repository.create_movie(movie)
    

    def get_movie_stats(self):
        return self.movie_repository.get_movie_stats()
    