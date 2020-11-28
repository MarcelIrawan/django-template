from rest_framework import serializers

from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    """
    Serilizer for user
    """
    class Meta:
        model = CustomUser
        # fields = '__all__'
        fields = ['id','email']