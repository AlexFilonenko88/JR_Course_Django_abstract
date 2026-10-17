from django.urls import path

from .views import (
    PostCreateView,
    PostDeleteView,
    PostDetailView,
    PostListView,
    PostUpdateView,
)

urlpatterns = [
    path("", PostListView.as_view(), name="post-list"),  # Список постов
    path(
        "post/<int:pk>/", PostDetailView.as_view(), name="post-detail"
    ),  # Детали поста
    path("post/new/", PostCreateView.as_view(), name="post-create"),  # Создание поста
    path(
        "post/<int:pk>/edit/", PostUpdateView.as_view(), name="post-update"
    ),  # Редактирование
    path(
        "post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"
    ),  # Удаление
]
