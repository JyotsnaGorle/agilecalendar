from agcal.models import User
from agcal.modules.session_keygen import SessionKeygen

import hashlib


class UserAuth:

    def __init__(self):
        self.response = {}
        self.loggedin_users = {}
        self.keygen = SessionKeygen()

    def _build_response(self, username, loggedin, sessionkey):
        self.response['username'] = username
        self.response['loggedin'] = loggedin
        self.response['sessionkey'] = sessionkey

    def login_user(self, username, password):
        users = User.objects.filter(
            username=username, password=hashlib.sha512(password).hexdigest())

        if users.count() == 0:
            self._build_response(username, False, None)
            return self.response

        if username not in self.loggedin_users:
            key = self.keygen.get_new_key()
            self.loggedin_users[username] = key
        else:
            key = self.loggedin_users[username]

        self._build_response(username, True, key)

        return self.response

    def logout_user(self, username):
        if username in self.loggedin_users:
            self.keygen.remove_key(self.loggedin_users[username])
            self.loggedin_users.pop(username, None)

        self._build_response(username, False, None)

        return self.response
