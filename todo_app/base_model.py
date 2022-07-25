from abc import abstractclassmethod
from django.db import models


class AbstractClass(models.Model):

    class Meta:
        abstract = True
