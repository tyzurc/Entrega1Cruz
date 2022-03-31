from django.shortcuts import render
from blog.models import *
from blog.forms import *

# Create your views here.

def inicio(request):
    return render(request, 'blog/inicio.html', {"title": "Inicio", "message": "¡Bienvenidx al blog!"})

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
            return render(request, 'blog/search_user.html', {"user": user, "title": "Búsqueda de usuarixs", "message": "Búsqueda de usuarixs"})
        except Exception as exc:
            print(exc)
            error = "No existe ese usuarix"
    return render(request, 'blog/search_user.html', {"error": error, "title": "Búsqueda de usuarixs", "message": "Búsqueda de usuarixs"})

def topics(request):
    topics = Topic.objects.all()

    if request.method == "POST":
        formulario = TopicsForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            topic = Topic(nombre=data['nombre'], descripcion=data['descripcion'])
            topic.save()

            formulario = TopicsForm()
            return render(request, 'blog/topics.html', {"topics": topics, "title": "Topicos", "message": "Todos los tópicos", "formulario": formulario})
    
    else:      
        formulario = TopicsForm()
        return render(request, 'blog/topics.html', {"topics": topics, "title": "Topicos", "message": "Todos los tópicos", "formulario": formulario})