from agcal.models import User
from agcal.modules.session_keygen import SessionKeygen
from agilecalendar.settings import SESSION_EXPIRY, REDIS_PASSWORD

import hashlib
import redis


class UserAuth:
    def __init__(self):
        self.response = {}
        self.logged_in_users = redis.StrictRedis(
            password=REDIS_PASSWORD)
        self.keygen = SessionKeygen()

    def _build_response(self, username, loggedin, sessionkey):
        self.response['username'] = username
        self.response['loggedin'] = loggedin
        self.response['sessionkey'] = sessionkey

    def login_user(self, username, password, ip, timestamp):
        users = User.objects.filter(
            username=username, password=hashlib.sha512(password).hexdigest())

        if users.count() == 0:
            self._build_response(username, False, None)
            return self.response

        key = self.keygen.get_key(username, ip, timestamp)
        self.logged_in_users.setex(key, SESSION_EXPIRY, 1)
        self._build_response(username, True, key)

        return self.response

    def logout_user(self, key):
        self.logged_in_users.delete(key)

        return "{'message': 'Ok'}"
