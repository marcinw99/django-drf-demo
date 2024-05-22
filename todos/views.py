from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from todos.models import Todo, Project
from todos.serializers import TodoSerializer, ProjectSerializer


@csrf_exempt
def projects(request):
    if request.method == "GET":
        all_projects = Project.objects.all()
        serializer = ProjectSerializer(all_projects, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ProjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
