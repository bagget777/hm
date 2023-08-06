from django.urls import path, include
from users import views

urlpatterns = [
    path("users/", include("django.contrib.auth.urls")),
    path("", views.UserRegisterView.as_view(), name="index-page"),
    path("users/register", views.register, name="register"),
]