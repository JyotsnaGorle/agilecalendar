from django.shortcuts import render
from django.http import HttpResponse
from agcal.modules.userauth import UserAuth
from agcal.modules.usermanager import UserManager

import json

userauth = UserAuth()
usermanager = UserManager()

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

def index(request):
    return render(request, 'agcal/index.html')


def login_user(request):
    if request.method != "POST" or not 'username' in request.POST or not 'password' in request.POST:
        return HttpResponse('{"error": "Invalid request"}', content_type="application/json")

    response = userauth.login_user(
        request.POST['username'], request.POST['password'])
    return HttpResponse(json.dumps(response), content_type="application/json")


def logout_user(request):
    if request.method != "POST" or not 'username' in request.POST:
        return HttpResponse('{"error": "Invalid request"}', content_type="application/json")

    response = userauth.logout_user(request.POST['username'])
    return HttpResponse(json.dumps(response), content_type="application/json")


def user(request):
    if request.method == "GET":
        if 'username' not in request.GET:
            response = '{"error": "Invalid request"}'
        else:
            response = usermanager.show_user(request.GET['username'])
    elif request.method == "PUT":
        request.PUT = morph_request(request, "PUT")

        if 'username' not in request.PUT or 'password' not in request.PUT or 'name' not in request.PUT or 'email' not in request.PUT:
            response = '{"error": "Invalid request"}'
        else:
            response = usermanager.add_user(
                PUT['username'], PUT['password'], PUT['name'], PUT['email'])
    elif request.method == "POST":
        if 'password' not in request.POST or 'name' not in request.POST or 'email' not in request.POST:
            response = '{"error": "Invalid request"}'
        else:
            response = usermanager.update_user(request.POST['username'], request.POST[
                                               'password'], request.POST['name'], request.POST['email'])
    elif request.method == "DELETE":
        request.DELETE = morph_request(request, "DELETE")

        if 'username' not in DELETE:
            response = '{"error": "Invalid request"}'
        else:
            response = usermanager.remove_user(DELETE['username'])
    else:
        response = '{"error": "Invalid request"}'

    return HttpResponse(response, content_type="application/json")


def card(request):
    pass
