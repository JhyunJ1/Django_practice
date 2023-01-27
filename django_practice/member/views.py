from django.shortcuts import render
from rest_framework import mixins, generics
from .serializers import CreateMemberSerializer

# Create your views here.

class CreateMember(
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    serializer_class = CreateMemberSerializer

    def get_queryset(self):
        return Member.objects.all()
    
    def post(self):
        pass
    
