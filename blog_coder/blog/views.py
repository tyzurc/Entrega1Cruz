from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post

# Create your views here.

def inicio(request):
    return render(request, 'blog/inicio.html', {"title": "Inicio", "message": "¡Bienvenidx!"})

def listar(request):
    posts = Post.objects.all()
    return render(request, 'blog/listar_posts.html', {"posts": posts, "title": "Posts", "message": "Todos los posts"})