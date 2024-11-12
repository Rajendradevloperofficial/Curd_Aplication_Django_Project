from app.models import register
from  rest_framework import serializers


class registerSerializer(serializers.ModelSerializer):
    class Meta:
        model=register
        fields=['id','name','email','password']