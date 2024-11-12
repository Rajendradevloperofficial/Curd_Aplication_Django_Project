from app.models import register
from app.api.serializers import registerSerializer
from rest_framework import viewsets

class registerViewSet(viewsets.ModelViewSet):
    queryset=register.objects.all()
    serializer_class=registerSerializer