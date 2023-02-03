from rest_framework import serializers
from .models import *


class DeskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desk
        fields = ('id', 'DeskName', 'Columns')


class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = ('id', 'ColumnName', 'Stories')


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ('id', 'StoryName', 'Description', 'DueDate',
                  'StoryEstimation', 'Tasks')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'TaskName', 'IsCompleted')
