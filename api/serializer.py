from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token


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
        Token.objects.create(user=user)
        return user
