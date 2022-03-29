from django.shortcuts import render
from django.http import HttpResponse
from blog.models import *

# Create your views here.

def inicio(request):
    return render(request, 'blog/inicio.html', {"title": "Inicio", "message": "¡Bienvenidx!"})

def posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/posts.html', {"posts": posts, "title": "Posts", "message": "Todos los posts"})

def users(request):
    users = User.objects.all()
    return render(request, 'blog/users.html', {"users": users, "title": "Usuarixs", "message": "Todxs los usuarixs"})