from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views
from .apiview import TestView, UserCreate

# 如果使用需要在setting文件打开默认token机制
# 默认的token机制 https://zhuanlan.zhihu.com/p/58426061
app_name = 'apis'
urlpatterns = [
    path('index', views.index),
    path('comments', views.comments),

    # 默认的token机制的注册和登录
    # path('register/', UserCreate.as_view(), name=UserCreate.name),
    # path('login/', LoginView.as_view(), name=LoginView.name),

    # 返回2个token:refresh access. 一个是刷新接口带的token 一个是其他接口带的token
    # https://zhuanlan.zhihu.com/p/139086573
    path('newregister/', UserCreate.as_view(), name=UserCreate.name),
    path('newlogin/', TokenObtainPairView.as_view(), name='login'),
    path('refreshtk/', TokenRefreshView.as_view(), name='refres_token'),
    path('test/', TestView.as_view(), name=TestView.name),
]
