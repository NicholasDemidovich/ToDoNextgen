from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

# Create your views here.


# Desk


class CreateDesk(generics.CreateAPIView):
    serializer_class = DeskSerializer


class DeleteDesk(generics.DestroyAPIView):
    serializer_class = DeskSerializer


class UpdateDesk(generics.RetrieveUpdateAPIView):
    serializer_class = DeskSerializer


class ListDesk(generics.ListAPIView):
    queryset = Desk.objects.all()
    serializer_class = DeskSerializer


# Column


class CreateColumn(generics.CreateAPIView):
    serializer_class = ColumnSerializer


class DeleteColumn(generics.DestroyAPIView):
    serializer_class = ColumnSerializer


class UpdateColumn(generics.RetrieveUpdateAPIView):
    serializer_class = ColumnSerializer


class ListColumn(generics.ListAPIView):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer


# Story


class CreateStory(generics.CreateAPIView):
    serializer_class = StorySerializer


class DeleteStory(generics.DestroyAPIView):
    serializer_class = StorySerializer


class UpdateStory(generics.RetrieveUpdateAPIView):
    serializer_class = StorySerializer


class ListStory(generics.ListAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer


# Task


class CreateTask(generics.CreateAPIView):
    serializer_class = TaskSerializer


class DeleteTask(generics.DestroyAPIView):
    serializer_class = TaskSerializer


class UpdateTask(generics.RetrieveUpdateAPIView):
    serializer_class = TaskSerializer


class ListTask(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
