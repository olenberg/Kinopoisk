from flask import request, abort
from flask_restx import Resource, Namespace
from app.implemented import auth_service, user_service

auth_ns = Namespace('auth')


@auth_ns.route('/login')
class AuthView(Resource):
    def post(self):
        data = request.json
        email = data.get("email", None)
        password = data.get("password", None)

        if None in [email, password]:
            abort(400)

        tokens = auth_service.generate_tokens(email, password)
        if not tokens:
            abort(401)

        return tokens, 201

    def put(self):
        data = request.json

        access_token = data.get("access_token")
        refresh_token = data.get("refresh_token")
        validate = auth_service.validate_tokens(access_token, refresh_token)

        if not validate:
            return "Invalid token", 400

        tokens = auth_service.approve_refresh_token(refresh_token)
        return tokens, 201


@auth_ns.route('/register')
class RegisterView(Resource):
    def post(self):
        req_json = request.json

        email = req_json.get("email")
        password = req_json.get("password")

        if None in [email, password]:
            return "", 400

        user_service.create(req_json)
        return f"Пользователь добавлен!", 201