import datetime
import calendar
import jwt
from flask import abort
from app.config import Config
from app.services.user import UserService


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_tokens(self, user_email, password, is_refresh=False):
        user = self.user_service.get_user_by_email(user_email)

        if user is None:
            abort(404)

        if not is_refresh:
            if not self.user_service.compare_passwords(user.password, password):
                abort(400)

        data = {
            "email": user.email,
            "role": user.role,
            "name": user.name,
            "id": user.id
        }

        # 30 minutes for access_token
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=Config.TOKEN_EXPIRE_MINUTES)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, Config.SECRET, algorithm=Config.ALGO)

        # 130 days for refresh_token
        min30 = datetime.datetime.utcnow() + datetime.timedelta(days=Config.TOKEN_EXPIRE_DAYS)
        data["exp"] = calendar.timegm(min30.timetuple())
        refresh_token = jwt.encode(data, Config.SECRET, algorithm=Config.ALGO)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }

    def approve_refresh_token(self, refresh_token):
        data = jwt.decode(jwt=refresh_token, key=Config.SECRET, algorithms=[Config.ALGO])
        mail_user = data.get("email")
        user = self.user_service.get_user_by_email(mail_user)

        if user is None:
            raise Exception()
        print(user, "service auth")
        return self.generate_tokens(mail_user, user.password, is_refresh=True)

    def validate_tokens(self, access_token, refresh_token):
        for token in [access_token, refresh_token]:
            try:
                jwt.decode(jwt=token, key=Config.SECRET, algorithms=[Config.ALGO])
            except Exception as e:
                print(e, 'validate not')
                return False

        return True
