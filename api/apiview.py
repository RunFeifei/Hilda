from django.contrib.auth import authenticate
from rest_framework import generics, status, permissions
# https://zhuanlan.zhihu.com/p/58426061
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt import authentication

from api.serializer import ApiUserSerializer


class UserCreate(generics.CreateAPIView):
    name = 'user_create'

    # 配置要使用的认证类，可以用如下方式配置（类属性方式）
    # authentication_classes = ()
    # 也可以用如下方式配置（实例方法）
    # 返回一个空的元组，表示从全局认证方式中豁免
    def get_authenticators(self):
        return ()

    # 返回一个空的元组，表是从全局认证方式中豁免
    def get_permissions(self):
        return ()

    def get_serializer_class(self):
        return ApiUserSerializer


class LoginView(APIView):
    name = 'login'

    def get_permissions(self):
        return ()

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return Response(
                data={
                    'token': user.auth_token.key
                }
            )
        else:
            return Response(
                data={
                    'token': 'fails'
                },
                status=status.HTTP_400_BAD_REQUEST
            )


class TestView(APIView):
    name = 'test'
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JWTAuthentication,)

    def get(self, request, *args, **kwargs):
        return Response('ok')
