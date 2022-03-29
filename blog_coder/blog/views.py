from django.shortcuts import render
from django.http import HttpResponse
from blog.models import *
from blog.forms import *

# Create your views here.

def inicio(request):
    return render(request, 'blog/inicio.html', {"title": "Inicio", "message": "¡Bienvenidx!"})

def posts(request):

    if request.method == "POST":
        formulario = PostsForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            post = Post(titulo=data['titulo'], contenido=data['contenido'], autorx=data['autorx'], fecha_creacion=data['fecha_creacion'])
            post.save()

            formulario = PostsForm()
            return render(request, 'blog/posts.html', {"posts": posts, "title": "Posts", "message": "Todos los posts", "formulario": formulario})
    
    else:      
        formulario = PostsForm()
        return render(request, 'blog/posts.html', {"posts": posts, "title": "Posts", "message": "Todos los posts", "formulario": formulario})

def users(request):
    users = User.objects.all()
    return render(request, 'blog/users.html', {"users": users, "title": "Usuarixs", "message": "Todxs los usuarixs"})