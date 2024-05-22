from django.urls import path
from todos import views

urlpatterns = [
    path('projects/', views.projects)
]
