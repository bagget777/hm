
from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post

def index_view(request):
    posts = Post.objects.all()
    context = {
        "title": "Главная страница",
        "posts": posts,
    }
    return render(request, "posts/index.html", context=context)


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, "posts/post_detail.html", {"post": post})

def post_update(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, "posts/post_update.html", {"post": post})

def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, "posts/post_delete.html", {"post": post})

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
