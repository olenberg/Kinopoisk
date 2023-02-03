from flask import request
from flask_restx import Resource, Namespace
from app.dao.models.genre import GenreSchema
from app.implemented import genre_service
from app.helpers.decorators import auth_required, admin_required

genres_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genres_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        filters = request.args
        all_genres = genre_service.get_all(filters)
        return genres_schema.dump(all_genres), 200


@genres_ns.route('/<int:gid>')
class GenreView(Resource):
    @auth_required
    def get(self, gid):
        genre = genre_service.get_one(gid)
        return genre_schema.dump(genre), 200
