import jwt
import base64
import hashlib
import hmac
from app.config import Config
from app.dao.user import UserDAO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_user_by_email(self, email):
        return self.dao.get_user_by_email(email)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        data["password"] = self.get_hash(data["password"])
        return self.dao.create(data)

    def update(self, data):
        self.dao.update(data)

    def update_password(self, passwords, email):
        new_password = self.get_hash(passwords.get('new_password'))
        self.dao.update_password(new_password, email)

    def delete(self, uid):
        self.dao.delete(uid)

    def get_user_email(self, token):
        try:
            data_token = jwt.decode(token, Config.SECRET, algorithms=[Config.ALGO])
            return data_token.get("email")
        except Exception as e:
            return f"{e}", 401

    def get_hash(self, password):
        return base64.b64encode(hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            Config.PWD_HASH_SALT,
            Config.PWD_HASH_ITERATIONS
        ))

    def compare_passwords(self, password_hash, other_password):
        return hmac.compare_digest(
            base64.b64decode(password_hash),
            hashlib.pbkdf2_hmac('sha256', other_password.encode(), Config.PWD_HASH_SALT, Config.PWD_HASH_ITERATIONS)
        )
