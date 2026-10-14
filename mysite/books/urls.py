from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.book_list, name="book_list"),
    path("<int:pk>/", views.book_detail, name="book_detail"),
    path("add/", views.book_add, name="book_add"),
    # path("books/", include(("books.urls", "books"), namespace="books")),
    path("add/", views.book_add, name="book_add"),
    path("genre/<str:genre>/year/<int:year>/", views.book_filter, name="book_filter"),
]
