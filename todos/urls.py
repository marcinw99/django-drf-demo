from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from todos import views

urlpatterns = [
    path('projects/', views.projects)
]

urlpatterns = format_suffix_patterns(urlpatterns)
