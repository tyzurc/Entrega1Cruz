from django.urls import path
from blog.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('posts/', posts, name="Posts"),
    path('users/', users, name="Usuarixs"),
    path('buscaruser/', search_user, name="BuscarUser"),
    path('topics/', topics, name="Topics"),
]