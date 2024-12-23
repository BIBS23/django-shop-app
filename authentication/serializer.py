from rest_framework import serializers
from .models import CustomUser,LoginModel

class UserSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(read_only=True)
    class Meta:
        model = CustomUser
        
        fields = ['email','mobile','password','user_id']
        extra_kwargs = {
            'password': {'write_only': True}, 
        }



class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginModel

        fields = '__all__'