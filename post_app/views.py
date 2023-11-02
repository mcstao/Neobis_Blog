from django.shortcuts import render
from django.views.generic import ListView

from post_app.models import Post


def home(request):
    if request.method == "GET":
        posts = Post.objects.all()
        context = {
            'posts': posts
        }
        return render(request, 'posts/home.html', context)


def post_detail_view(request, post_id):
    if request.method == "GET":
        post = Post.objects.get(id=post_id)
        context = {
            'post': post
        }
        return render(request, 'posts/post_detail.html', context)
