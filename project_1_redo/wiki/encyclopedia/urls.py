from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create_page", views.create, name="create"),
    path("random", views.random, name="random"),
    path("search", views.search, name="search"),
    path("<str:name>", views.entry, name="entry"),
    path("wiki/<str:name>", views.entry, name="entry"),
    path("edit/<str:name>", views.edit, name="edit"),

]
