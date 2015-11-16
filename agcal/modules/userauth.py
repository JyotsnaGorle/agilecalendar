from agcal.models import User
from agcal.modules.session_keygen import SessionKeygen

import hashlib


class UserAuth:

    def __init__(self):
        self.response = {}
        self.logged_in_users = {}
        self.keygen = SessionKeygen()

    def _build_response(self, username, loggedin, sessionkey):
        self.response['username'] = username
        self.response['loggedin'] = loggedin
        self.response['sessionkey'] = sessionkey

    def login_user(self, username, password, ip):
        users = User.objects.filter(
            username=username, password=hashlib.sha512(password).hexdigest())

        if users.count() == 0:
            self._build_response(username, False, None)
            return self.response

        if username not in self.logged_in_users:
            self.logged_in_users[username] = {}
            self.logged_in_users[username][ip] = self.keygen.get_new_key()
        elif ip not in self.logged_in_users[username]:
            self.logged_in_users[username][ip] = self.keygen.get_new_key()

        self._build_response(username, True, self.logged_in_users[username][ip])

        return self.response

    def logout_user(self, username, ip):
        if username in self.logged_in_users:
            self.keygen.remove_key(self.logged_in_users[username][ip])
            self.logged_in_users[username].pop(ip, None)

            if len(self.logged_in_users[username].keys()) == 0:
                self.logged_in_users.pop(username, None)

        self._build_response(username, False, None)

        return self.response
