from rest_framework import serializers
from .. import models


class TodoViewSerializer(serializers.ModelSerializer):
    class meta:
        model = models.Todo
        fields = "__all__"
