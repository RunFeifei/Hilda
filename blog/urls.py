from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('blog', views.index, name='index'),
    path('blog/post/<int:pk>/', views.detail, name='detail'),
    path('blog/post/<int:year>/<int:month>/', views.archives, name='archive'),
    path('blog/categories/<int:pk>/', views.category, name='category'),
    path('blog/tags/<int:pk>/', views.tag, name='tag'),
]
