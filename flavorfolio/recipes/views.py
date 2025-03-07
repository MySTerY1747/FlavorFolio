from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    context_dict = {"body_block": "This is the index page.", "title_block": "Index"}
    response = render(request, "recipes/base.html", context=context_dict)
    return response


def about(request):
    context_dict = {"body_block": "This is the about page.", "title_block": "About"}
    response = render(request, "recipes/base.html", context=context_dict)
    return response
