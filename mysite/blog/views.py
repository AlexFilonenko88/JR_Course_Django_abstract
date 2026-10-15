from django.views.generic import DetailView, ListView

from .models import Post


class PostListView(ListView):
    model = Post  # Указываем модель
    template_name = "post_list.html"  # Ваш шаблон для отображения
    context_object_name = "posts"  # Имя переменной контекста для списка объектов


class PostDetailView(DetailView):
    model = Post  # Модель, с которой работает представление
    template_name = "post_detail.html"  # Шаблон для отображения деталей
    context_object_name = "post"  # Имя переменной контекста
