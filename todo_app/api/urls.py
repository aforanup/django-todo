from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('todo/', views.UserTodoView.as_view(), name='home'),
    path("todo/<int:id>", views.UserTodoDetailView.as_view(), name='detail'),
]
