from django.shortcuts import render
from django.http import HttpResponse
from agcal.modules.userauth import UserAuth

import json

userauth = UserAuth()


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
    return HttpResponse(request.method, content_type="text/plain")


def card(request):
    pass
