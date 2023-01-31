from app.dao.user import UserDAO
from app.dao.movie import MovieDAO
from app.dao.director import DirectorDAO
from app.dao.genre import GenreDAO
from app.setup_db import db
from app.services.user import UserService
from app.services.auth import AuthService
from app.services.movie import MovieService
from app.services.director import DirectorService
from app.services.genre import GenreService

user_dao = UserDAO(db.session)
user_service = UserService(dao=user_dao)

auth_service = AuthService(user_service=user_service)

movie_dao = MovieDAO(db.session)
movie_service = MovieService(dao=movie_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(dao=director_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(dao=genre_dao)