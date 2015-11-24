import hashlib
import json

import redis

from agcal.models import User
from agcal.modules.session_keygen import SessionKeygen
from agilecalendar.settings import SESSION_EXPIRY, REDIS_PASSWORD


class UserAuth:
    def __init__(self):
        self.response = {}
        self.logged_in_users = redis.StrictRedis(password=REDIS_PASSWORD)
        self.keygen = SessionKeygen()

    def _build_response(self, username, logged_in, session_key):
        self.response['username'] = username
        self.response['loggedin'] = logged_in
        self.response['sessionkey'] = session_key

    def login_user(self, username, password, ip):
        users = User.objects.filter(username=username, password=hashlib.sha512(password).hexdigest())

        if users.count() == 0:
            self._build_response(username, False, None)
            return (self.response, 403)

        value = self.keygen.get_key(username, ip)
        key = hashlib.sha256(value).hexdigest()

        self.logged_in_users.setex(key, SESSION_EXPIRY, value)
        self._build_response(username, True, key)

        return (self.response, 200)

    def logout_user(self, username, key):
        status = 403
        value = self.logged_in_users.get(key)

        if not value:
            message = 'Invalid/Expired Session'
        elif json.loads(self.keygen.get_info(value))['username'] != username:
            message = 'Session key mismatch'
        else:
            self.logged_in_users.delete(key)
            message = "Ok"
            status = 200

        return ('{"message": "%s"}' % message, status)
