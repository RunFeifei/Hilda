from django.contrib.auth.models import User
from jwt.compat import text_type
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken


# 注册使用
# 默认token
class ApiUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'pk',
            'username',
            'email',
            'password',
        ]
        # password不暴露在response中去
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        # 使用user.set_password()
        # 对密码编码，而不使用原始字符作为密码
        user.set_password(validated_data['password'])
        user.save()
        # 保存User实例后，在Token模型（数据库表）中，也对应保存一个Token实例作为用户的token
        # 这种是默认机制的token
        Token.objects.create(user=user)
        return user


# 注册使用
# simple jwt的token
# 注册同时返回token
class ApiUserSerializer2(serializers.ModelSerializer):
    tokens = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'pk',
            'username',
            'email',
            'password',
            'tokens',
        ]
        # password不暴露在response中去
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def get_tokens(self, user):
        tokens = RefreshToken.for_user(user)
        refresh = text_type(tokens)
        access = text_type(tokens.access_token)
        data = {
            "refresh": refresh,
            "access": access
        }
        return data

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        # 使用user.set_password()
        # 对密码编码，而不使用原始字符作为密码
        user.set_password(validated_data['password'])
        user.save()
        # 保存User实例后，在Token模型（数据库表）中，也对应保存一个Token实例作为用户的token
        # 这种是默认机制的token
        # Token.objects.create(user=user)
        return user
