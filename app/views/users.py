from flask import request
from flask_restx import Resource, Namespace
from app.implemented import user_service
from app.dao.models.user import UserSchema
from app.helpers.decorators import auth_required

user_ns = Namespace('user')

user_schema = UserSchema()

@user_ns.route('/')
class UserView(Resource):
    @auth_required
    def get(self):
        auth_data = request.headers['Authorization']
        token = auth_data.split("Bearer ")[-1]
        email = user_service.get_email(token)
        user = user_service.get_user_by_email(email)

        return user_schema.dump(user), 200

    @auth_required
    def patch(self):
        data = request.json
        user_service.update(data)

        return "", 204


@user_ns.route('/password/')
class PasswordView(Resource):
    @auth_required
    def put(self):
        auth_data = request.headers['Authorization']
        token = auth_data.split("Bearer ")[-1]
        email = user_service.get_email(token)
        passwords = request.json
        user_service.update_password(passwords, email)

        return "", 204



