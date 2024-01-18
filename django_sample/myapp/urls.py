from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("<uuid:employee_id>/", views.detail, name="detail"),
    path("delete/<uuid:employee_id>/", views.delete, name="delete"),
]
