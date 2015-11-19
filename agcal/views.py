from django.shortcuts import render
from django.http import HttpResponse
from agcal.modules.userauth import UserAuth
from agcal.modules.usermanager import UserManager
import json
import time

userauth = UserAuth()
user_manager = UserManager()


def morph_request(request, method):
    if hasattr(request, '_post'):
        del request._post
        del request._files

    try:
        request.method = "POST"
        request._load_post_and_files()
        request.method = method
    except AttributeError:
        request.META['REQUEST_METHOD'] = 'POST'
        request._load_post_and_files()
        request.META['REQUEST_METHOD'] = method

    return request.POST


def get_time():
    return str(int(time.time() * 1000))


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')

    return ip


def is_sublist(sub_list, super_list):
    return set(sub_list).issubset(set(super_list))


def index(request):
    return render(request, 'agcal/index.html')


def login_user(request):
    if request.method != "POST" or not is_sublist(['username', 'password'], request.POST):
        return HttpResponse('{"message": "Invalid request"}', content_type="application/json", status=400)

    response = userauth.login_user(
        request.POST['username'], request.POST['password'], get_client_ip(request), get_time())

    return HttpResponse(json.dumps(response), content_type="application/json")


def logout_user(request):
    if request.method != "POST" or 'key' not in request.POST:
        return HttpResponse('{"message": "Invalid request"}', content_type="application/json", status=400)

    response = userauth.logout_user(request.POST['key'])

    return HttpResponse(json.dumps(response), content_type="application/json")


def user(request, username=None):
    status = 200

    if request.method == "GET":
        if not username:
            response = '{"message": "Invalid request"}'
            status = 400
        else:
            response = user_manager.show_user(username)
    elif request.method == "PUT":
        request.PUT = morph_request(request, "PUT")

        if not is_sublist(['username', 'password', 'name', 'email'], request.PUT):
            response = '{"message": "Invalid request"}'
            status = 400
        else:
            response = user_manager.add_user(
                request.PUT['username'], request.PUT['password'], request.PUT['name'], request.PUT['email'])
    elif request.method == "POST":
        if not is_sublist(['password', 'name', 'email'], request.POST):
            response = '{"message": "Invalid request"}'
            status = 400
        else:
            response = user_manager.update_user(request.POST['username'], request.POST[
                'password'], request.POST['name'], request.POST['email'])
    elif request.method == "DELETE":
        request.DELETE = morph_request(request, "DELETE")

        if not username:
            response = '{"message": "Invalid request"}'
            status = 400
        else:
            response = user_manager.remove_user(username)
    else:
        response = '{"message": "Invalid request"}'
        status = 400

    return HttpResponse(response, content_type="application/json", status=status)


def card(request):
    pass
