from rest_framework import serializers
from .models import Cam



class CamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cam
        fields = '__all__'