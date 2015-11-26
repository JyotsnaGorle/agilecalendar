import hashlib
import json

import redis
from django.contrib.auth.hashers import check_password

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

    def _get_user(self, key):
        value = self.logged_in_users.get(key)

        if value:
            return json.loads(self.keygen.get_info(value))['username']

    def login_user(self, username, password, ip):
        try:
            user = User.objects.get(username=username)
        except Exception:
            self._build_response(username, False, None)
            return (self.response, 403)

        if not check_password(password, user.password):
            self._build_response(username, False, None)
            return (self.response, 403)

        value = self.keygen.get_key(username, ip)
        key = hashlib.sha256(value).hexdigest()

        self.logged_in_users.setex(key, SESSION_EXPIRY, value)
        self._build_response(username, True, key)

        return (self.response, 200)

    def logout_user(self, username, key):
        if self._get_user(key) != username:
            message = 'Invalid/Expired Session'
            status = 403
        else:
            self.logged_in_users.delete(key)
            message = "ok"
            status = 200

        return ('{"message": "%s"}' % message, status)

    def is_valid_user(self, username, key):
        return self._get_user(key) == username

    def reset_expiry_for(self, key):
        self.logged_in_users.expire(key, SESSION_EXPIRY)
