from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ["id","name","age","gender","height","weight","ap_hi","ap_lo","cholesterol","gluc","smoke","alco","active","cardisrate"]


class UserResponseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ["id","name","cardisrate"]



