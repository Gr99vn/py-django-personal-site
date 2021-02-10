from django.urls import path
from . import views

urlpatterns = [
  path("", views.blog_index, "blog_index"),
  path("<int:pk>/", views.blog_detail, "blog_detail"),
  path("<category>/", views.blog_category, "blog_category"),
]