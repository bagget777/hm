
from django.shortcuts import render
from django.http import HttpResponse

def index_view(request):
    context = {
        'title': "Главная страница"
    }
    return render(request, "posts/index.html", context=context)

def contacts(request,):
    context = {
        "title": "Контакты"
    }
    return render(request, "posts/contacts.html", context)

def about(request):
    context = {
        "title": "Про меня"
    }
    return render(request, "posts/about.html", context)
