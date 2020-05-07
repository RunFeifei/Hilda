from django.urls import path

from . import views

app_name = 'apis'
urlpatterns = [
    path('index', views.index),
    path('comments', views.comments),
]
