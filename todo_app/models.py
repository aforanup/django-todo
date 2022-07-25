from todo_app.base_model import AbstractClass
from django.db import models

from django.contrib.auth.models import AbstractBaseUser


class User(AbstractClass, AbstractBaseUser):
    first_name = models.CharField(max_length=125)

    def __str__(self) -> str:
        return self.first_name


class Picture(AbstractClass):
    image = models.ImageField()


class TodoType(AbstractClass):
    label = models.CharField(max_length=125)
    picture = models.ForeignKey(Picture, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.label


class Todo(AbstractClass):
    type = models.ForeignKey(TodoType, null=True, on_delete=models.SET_NULL)
    note = models.TextField()
    picture = models.ForeignKey(Picture, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.type.label
