from flask import request
from flask_restx import Resource, Namespace
from app.dao.models.movie import MovieSchema
from app.implemented import movie_service
from app.helpers. decorators import auth_required, admin_required

movies_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

@movies_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        filters = request.args
        all_movies = movie_service.get_all(filters)
        return movies_schema.dump(all_movies), 200


@movies_ns.route('/<int:mid>')
class DirectorView(Resource):
    @auth_required
    def get(self, mid):
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie), 200
