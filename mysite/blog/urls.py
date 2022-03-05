from django.urls import path
from . import views

urlpatterns = [
    #This pattern will tell Django that views.post_list is the place to go if someone enters your site at 'http://127.0.0.1:8000/'.
    #name='post_list' = view 
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
