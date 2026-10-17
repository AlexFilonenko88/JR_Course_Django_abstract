from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"  # По умолчанию: <app>/<model>_list.html
    context_object_name = "posts"  # По умолчанию: object_list
    ordering = ["-created_at"]  # Сортировка: новые посты сверху


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"  # По умолчанию: <app>/<model>_detail.html
    context_object_name = "post"  # По умолчанию: object


class PostCreateView(CreateView):
    model = Post
    fields = ["title", "content"]  # Поля, которые нужно отобразить в форме
    template_name = "blog/post_form.html"  # По умолчанию: <app>/<model>_form.html


class PostUpdateView(UpdateView):
    model = Post
    fields = ["title", "content"]
    template_name = "blog/post_form.html"


class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("post-list")  # Куда перейти после успешного удаления
