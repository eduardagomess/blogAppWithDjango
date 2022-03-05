from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    #para cada URL que começa com admin/, o Django irá encontrar uma view correspondente
    path('admin/', admin.site.urls),
    #Django agora irá redirecionar 'http://127.0.0.1:8000 /'para blog.urls
    path('', include('blog.urls')),
]
