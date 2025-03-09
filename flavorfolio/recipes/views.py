from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    context_dict = {"body_block": "This is the index page.", "title_block": "Index"}
    response = render(request, "recipes/index.html", context=context_dict)
    return response

def register(request):
    return render(request, 'recipes/register.html',context={})
