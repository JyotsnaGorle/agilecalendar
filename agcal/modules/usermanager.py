from agcal.models import User


class UserManager:
    @staticmethod
    def show_user(username):
        usernames = User.objects.filter(username=username)

        if not usernames.count():
            response = '{"message": "No such user"}'
            status = 404
        else:
            user = usernames.first()
            response = '{"username": "%s", "name": "%s", "email": "%s"}' % (
                user.username, user.name, user.email)
            status = 200

        return (response, status)

    @staticmethod
    def check_username_email(username, email):
        response = '{"message": "Ok"}'
        status = 200

        if User.objects.filter(username=username).count():
            response = '{"message": "Username Exists"}'
            status = 409

        if User.objects.filter(email=email).count():
            response = '{"message": "Email Exists"}'

        return (response, status)

    @staticmethod
    def add_user(username, password, name, email):
        user = User(username, password, name, email)

        user_status = UserManager.check_username_email(username, email)
        if user_status[1] == 409:
            return user_status

        user.save()
        response = '{"message": "ok"}'
        status = 200

        return (response, status)

    @staticmethod
    def remove_user(username):
        usernames = User.objects.filter(username=username)

        if not usernames.count():
            response = '{"message": "No such user"}'
            status = 404
        else:
            usernames.first().delete()
            response = '{"message": "ok"}'
            status = 200

        return (response, status)

    @staticmethod
    def update_user(username, password, name, email):
        try:
            user = User.objects.get(username=username)
        except Exception:
            response = '{"message": "No such user"}'
            status = 404
        else:
            user.password = password
            user.name = name
            user.email = email
            user.save()
            response = '{"message": "ok"}'
            status = 200

        return (response, status)
