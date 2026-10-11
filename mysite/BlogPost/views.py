# BlogPost/views.py
from django.shortcuts import render

from .models import Post


def blog_posts(request):
    posts = Post.objects.all()
    return render(request, "BlogPost/blog_posts.html", {"posts": posts})
