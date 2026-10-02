from django.urls import include, path
from two_factor.urls import urlpatterns as tf_urls
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("<uuid:employee_id>/", views.detail, name="detail"),
    path("delete/<uuid:employee_id>/", views.delete, name="delete"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("", include(tf_urls)),
]
