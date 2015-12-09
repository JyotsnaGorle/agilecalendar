from agcal.models import User


def show_user(username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        response = '{"message": "No such user"}'
        status = 404
    else:
        response = '{"username": "%s", "name": "%s", "email": "%s"}' % (user.username, user.name, user.email)
        status = 200

    return response, status


def check_username_email(username, email):
    response = '{"message": "ok"}'
    status = 200

    if User.objects.filter(username=username).exists():
        response = '{"message": "Username Exists"}'
        status = 409

    if User.objects.filter(email=email).exists():
        response = '{"message": "Email Exists"}'

    return response, status


def add_user(username, password, name, email):
    user = User(username, password, name, email)

    user_status = check_username_email(username, email)
    if user_status[1] == 409:
        return user_status

    user.save()
    response = '{"message": "ok"}'
    status = 200

    return response, status


def remove_user(username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        response = '{"message": "No such user"}'
        status = 404
    else:
        user.delete()
        response = '{"message": "ok"}'
        status = 200

    return response, status


def update_user(username, password, name, email):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        response = '{"message": "No such user"}'
        status = 404
    else:
        user.password = password
        user.name = name
        user.email = email
        user.save()
        response = '{"message": "ok"}'
        status = 200

    return response, status
