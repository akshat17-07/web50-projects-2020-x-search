from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("/create_page", views.createpage, name="createpage"),
    path("<str:name>", views.pages, name="pages"),
    path("<str:name>", views.edit, name="edit")
]
