from django.shortcuts import render

from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from django.contrib import auth


class RegisterView(GenericAPIView):
  serializer_class = UserSerializer

  def post(self, request):
    serializer = UserSerializer(data={render.data})
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)