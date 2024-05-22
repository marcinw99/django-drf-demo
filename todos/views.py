from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
# from rest_framework.views import APIView

from todos.models import Todo, Project
from todos.serializers import TodoSerializer, ProjectSerializer


@api_view(['GET', 'POST'])
def projects(request, format=None):
    if request.method == "GET":
        all_projects = Project.objects.all()
        serializer = ProjectSerializer(all_projects, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ProjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ProjectsAPIView(APIView):
#     def GET(self, request):
#         all_projects = Project.objects.all()
#         serializer = ProjectSerializer(all_projects, many=True)
#         return Response(serializer.data)
