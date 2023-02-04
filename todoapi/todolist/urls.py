from django.urls import path
from .views import *


urlpatterns = [
    # Desk

    path('<int:pk>/', UpdateDesk.as_view()),
    path('', ListDesk.as_view()),
    path('create', CreateDesk.as_view()),
    path('delete/<int:pk>', DeleteDesk.as_view()),

    # Column

    path('<int:pk>/', UpdateColumn.as_view()),
    path('', ListColumn.as_view()),
    path('create', CreateColumn.as_view()),
    path('delete/<int:pk>', DeleteColumn.as_view()),

    # Story

    path('<int:pk>/', UpdateStory.as_view()),
    path('', ListStory.as_view()),
    path('create', CreateStory.as_view()),
    path('delete/<int:pk>', DeleteStory.as_view()),

    # Task

    path('<int:pk>/', UpdateTask.as_view()),
    path('', ListTask.as_view()),
    path('create', CreateTask.as_view()),
    path('delete/<int:pk>', DeleteTask.as_view())
]