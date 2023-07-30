
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from posts.models import Post
from django.views import generic
 # Класс Retrieve LIST
class IndexView(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=True)
    template_name = "posts/index.html"
    context_object_name = "posts"
    
 # Класс Retrieve DETAIL 
class PostDetailView(generic.DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    context_object_name = "post"
    
 # Класс Create
class PostCreateView(generic.CreateView):
    model = Post
    template_name = "posts/post_create.html"
    fields = ["title", "content", "status", "category", "cover"]
    success_url = reverse_lazy("post-verification")
    
 # Класс DELETE
class PostDeleteView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy("index-page")

def post_verification(request):
    context = {
        "title": "Страница верификации",
    }
    return render(request, "posts/post_verification.html", context=context)

 # CRUD = Create, Read(Retrieve), Update, Delete
 # Retrieve
def index_view(request):
    posts = Post.objects.all()
    context = {
        "title": "Главная страница",
        "posts": posts,
    }
    return render(request, "posts/index.html", context=context)
 # Retrieve
 
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, "posts/post_detail.html", {"post": post})

def contacts(request):
    context = {
        "title": "Контакты"
    }
    return render(request, "posts/contacts.html", context)

def about(request):
    context = {
        "title": "О нас"
    }
    return render(request, "posts/about.html", context)
def post_update(request, pk):
    return render(request, "posts/post_update.html")


