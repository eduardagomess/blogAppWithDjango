from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    # for each URL that starts with admin/, Django will find a corresponding view
    path('admin/', admin.site.urls),
    #Django irá redirecionar 'http://127.0.0.1:8000 /'para blog.urls
    path('', include('blog.urls')),
]
