from datetime import datetime
import hashlib
import base64
import hmac
from app.config import Config
from app.dao.models.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_user_by_email(self, email):
        return self.session.query(User).filter(User.email == email).first()

    def get_all(self):
        return self.session.query(User).all()

    def create(self, data):
        user = User(**data)
        self.session.add(user)
        self.session.commit()
        return user

    def update(self, data):
        user = self.get_one(data.get("id"))
        data['created_on'] = datetime.fromisoformat(data['created_on'])
        data['updated_on'] = datetime.now()

        for k, v in data.items():
            setattr(user, k, v)

        self.session.add(user)
        self.session.commit()

    def update_password(self, new_password, email):
        user = self.get_user_by_email(email)
        user.password = new_password
        self.session.add(user)
        self.session.commit()

    def delete(self, uid):
        user = self.get_one(uid)
        self.session.delete(user)
        self.session.commit()

    def compare_passwords(self, password_hash, other_password) -> bool:
        return hmac.compare_digest(
            base64.b64decode(password_hash),
            hashlib.pbkdf2_hmac(
                'sha256',
                other_password.encode('utf-8'),
                Config.PWD_HASH_SALT,
                Config.PWD_HASH_ITERATIONS
            )
        )
