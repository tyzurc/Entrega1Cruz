from django.shortcuts import render
from blog.models import *
from blog.forms import *

# Create your views here.

def inicio(request):
    return render(request, 'blog/inicio.html', {"title": "Inicio", "message": "¡Bienvenidx!"})

def posts(request):
    posts = Post.objects.all()

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

    if request.method == "POST":
        formulario = UsersForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            user = User(nombre=data['nombre'], user_name=data['user_name'], email=data['email'])
            user.save()

            formulario = UsersForm()
            return render(request, 'blog/users.html', {"users": users, "title": "Usuarixs", "message": "Todxs los usuarixs", "formulario": formulario})
    
    else:      
        formulario = UsersForm()
        return render(request, 'blog/users.html', {"users": users, "title": "Usuarixs", "message": "Todxs los usuarixs", "formulario": formulario})

def search_user(request):

    data = request.GET.get('user_name', "")
    error = ""

    if data:
        try:
            user = User.objects.get(user_name=data)
            return render(request, 'blog/search_user.html', {"user": user})
        except Exception as exc:
            print(exc)
            error = "No existe ese usuarix"
    return render(request, 'blog/search_user.html', {"error": error})