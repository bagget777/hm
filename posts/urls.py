from django.urls import path
from posts import views


urlpatterns = [
    path("", views.index_view, name="index-page"),
    path("contacts/", views.contacts, name="contacts-page"),
    path("about/", views.about, name="about-page"),
]