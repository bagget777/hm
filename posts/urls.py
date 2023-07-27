from django.urls import path
from posts import views


urlpatterns = [
    path("", views.index_view, name="index-page"),
    path("contacts/", views.contacts, name="contacts-page"),
    path("about/", views.about, name="about-page"),
    path("post/<int:pk>", views.post_detail, name="post-detail"),
    path("post_update/<int:pk>", views.post_update, name="post_update"),
    path("post_delete/<int:pk>", views.post_delete, name="post_delete"),
]