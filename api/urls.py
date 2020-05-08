from django.urls import path

from . import views
from .apiview import UserCreate, LoginView

app_name = 'apis'
urlpatterns = [
    path('index', views.index),
    path('comments', views.comments),
    path('user/', UserCreate.as_view(), name=UserCreate.name),
    path('login/', LoginView.as_view(), name=LoginView.name),
]
