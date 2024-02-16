from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list, name="posts"),
    path("create/", views.create_post, name="create-post"),
    path("edit-post/<str:pk>/", views.edit_post, name="edit-post"),
    path("edit-comment/<str:pk>/", views.edit_comment, name="edit-comment"),
    path("delete-post/<str:pk>/", views.delete_post, name="delete-post"),
    path("delete-comment/<str:pk>/", views.delete_comment, name="delete-comment"),
    path("post/<str:pk>/", views.post_detail, name="post-detail"),
    path("post/<str:pk>/", views.post_detail, name="post-detail"),
    path("post/<str:pk>/add-comment/", views.create_comment, name="create-comment"),
]
