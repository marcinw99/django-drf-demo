from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from todos import views

urlpatterns = [
    path('projects/', views.ProjectsAPIView.as_view()),
    path('todos/', views.TodosAPIView.as_view()),
    path('todos/<int:pk>/', views.TodoAPIView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
