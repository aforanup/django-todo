from rest_framework.response import Response
from .. import models
from . import serializers


class UserTodoView():
    def get(self, request, *args, **kwargs):
        todo = models.Todo.objects.all()
        serializer = serializers.TodoSerializer(todo, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = serializers.TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


class UserDetailView():
    def get(self, request, id, *args, **kwargs):
        todo = models.Todo.objects.filter(id=id).first()
        serializer = serializers.TodoSerializer(todo)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        todo = models.Todo.objects.filter(id=id).first()
        serializer = serializers.TodoSerializer(
            todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, id, *args, **kwargs):
        todo = models.Todo.objects.filter(id=id).first()
        todo.delete()
        return Response({"message": "successfully deleted"}, status=200)
