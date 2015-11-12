from agcal.models import User

import hashlib


class UserManager:

    def show_user(self, username):
        usernames = User.objects.filter(username=username)

        if not usernames.count():
            response = '{"error": "No such user"}'
        else:
            user = usernames.first()
            response = '{"username": "%s", "name": "%s", "email": "%s"}' % (
                user.username, user.name, user.email)

        return response

    def add_user(self, username, password, name, email):
        user = User(username, password, name, email)

        usernames = User.objects.filter(username=username)
        emails = User.objects.filter(email=email)

        if usernames.count():
            response = '{"error": "Username Exists"}'
        elif emails.count():
            response = '{"error": "Email Exists"}'
        else:
            user.save()
            response = '{"message": "ok"}'

        return response

    def remove_user(self, username):
        usernames = User.objects.filter(username=username)

        if not usernames.count():
            response = '{"error": "No such user"}'
        else:
            usernames.first().delete()
            response = '{"message": "ok"}'

        return response

    def update_user(self, username, password, name, email):
        usernames = User.objects.filter(username=username)

        if not usernames.count():
            response = '{"error": "No such user"}'
        else:
            user = usernames.first()
            user.password = hashlib.sha512(password).hexdigest()
            user.name = name
            user.email = email
            user.save()
            response = '{"message": "ok"}'

        return response
