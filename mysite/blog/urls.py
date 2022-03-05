from django.urls import path
from . import views

urlpatterns = [
    #Este padrão dirá ao Django que views.post_list é o lugar para ir se alguém entra em seu site pelo endereço 'http://127.0.0.1:8000 /'.
    #name='post_list', é o nome da URL que será usado para identificar a view
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
