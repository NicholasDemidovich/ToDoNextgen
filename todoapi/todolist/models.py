from django.db import models

# Create your models here.


class Desk(models.Model):
    DeskName = models.CharField('Desk name', max_length=100, blank=False)


class Column(models.Model):
    ColumnName = models.CharField('Column name', max_length=100, blank=False)
    Desk = models.ForeignKey(Desk, related_name='Columns', on_delete=models.CASCADE)


class Story(models.Model):
    StoryName = models.CharField('Story name', max_length=100, blank=False)
    Description = models.CharField('Description', max_length=300, blank=False)
    DueDate = models.DateField('Date of completion', blank=False)
    StoryEstimation = models.IntegerField('Story estimation', blank=False)
    Column = models.ForeignKey(Column, related_name='Stories', on_delete=models.CASCADE)


class Task(models.Model):
    TaskName = models.CharField('Task name', max_length=50, blank=False)
    IsCompleted = models.BooleanField('Completed', blank=False)
    Story = models.ForeignKey(Story, related_name='Tasks', on_delete=models.CASCADE)
