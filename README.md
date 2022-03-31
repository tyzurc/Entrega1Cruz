# Blog-coder
Se trata de una web tipo blog realizada utilizando el framework de Django como proyecto final del curso de Python en CoderHouse.

## Instrucciones de uso

1. Clonar el proyecto
2. Instalar las dependencias del proyecto: `pip install django`
3. Crear las migraciones ejecutando `python manage.py makemigrations` y luego `python manage.py migrate`
4. Iniciar la aplicación con `python manage.py runserver`

Una vez inicializada la aplicación, tendrás disponible para visitar la url de [Inicio](http://127.0.0.1:8000/blog/) y navegar dentro de las distintas páginas disponibles actualmente.

### Páginas

-[Posts](http://127.0.0.1:8000/blog/posts/)
  En esta página podrás crear posts y visualizar todos los agregados
-[Usuarixs](http://127.0.0.1:8000/blog/users/)
  En esta página podrás crear usuarixs y visualizar todos los agregados
-[Búsqueda de usuarixs](http://127.0.0.1:8000/blog/buscaruser/)
  En esta página podrás realizar una búsqueda de usuarixs
-[Tópicos](http://127.0.0.1:8000/blog/topics/)
  En esta página podrás crear tópicos y visualizar todos los agregados
