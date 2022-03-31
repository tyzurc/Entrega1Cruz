from django import forms

class PostsForm(forms.Form):
    titulo = forms.CharField(max_length=60)
    contenido = forms.CharField(max_length=200)
    autorx = forms.CharField(max_length=60)
    fecha_creacion = forms.DateField()

class UsersForm(forms.Form):
    nombre = forms.CharField(max_length=60)
    user_name = forms.CharField(max_length=60)
    email = forms.CharField(max_length=60)

class TopicsForm(forms.Form):
    nombre = forms.CharField(max_length=60)
    descripcion = forms.CharField(max_length=120)