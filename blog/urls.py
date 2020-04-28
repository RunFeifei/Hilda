from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>/', views.detail, name='detail'),
    path('post/<int:year>/<int:month>/', views.archives, name='archive'),
    path('categories/<int:pk>/', views.category, name='category'),
    path('tags/<int:pk>/', views.tag, name='tag'),
]
