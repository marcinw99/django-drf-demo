from rest_framework import serializers
from todos.models import Project, Todo


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title']


class TodoSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())

    class Meta:
        model = Todo
        fields = ['id', 'label', 'completed', 'completed_at', 'category', 'project']
