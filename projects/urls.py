from django.urls import path
from . import views

urlpatterns = [
  path("", view=views.project_index, name="project_index"),
  path("<int:pk>/", view=views.project_detail, name="project_detail"),
]