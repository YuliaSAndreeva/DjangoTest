from django.contrib.auth.models import Group
from django.shortcuts import render
from pyexpat.errors import messages
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework.views import APIView



from .serializers import GroupSerializer


@api_view()
def hello_world(request: Request) -> Response:
    return Response({'message': 'Hello. world!'} )


# class GroupListAPIView(APIView):
#     def get(self, request: Request) -> Response:
#         groups = Group.objects.all()
#
#         serializer = GroupSerializer(groups, many=True)
#         # data = [group.name for group in groups]
#         return Response({'groups': serializer.data})

class GroupListAPIView(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
