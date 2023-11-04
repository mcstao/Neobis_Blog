from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from post_app.forms import PostCreateForm
from post_app.models import Post


def home(request):
    if request.method == "GET":
        posts = Post.objects.all().order_by('-post_date')

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

@login_required
def add_post(request):
    if request.method == "POST":
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Пост успешно добавлен")
            return redirect('home')
    else:
        form = PostCreateForm()


    context = {
        'form': form
    }
    return render(request, 'posts/add_post.html', context)

def update_post(request, post_id):
    new_post = Post.objects.get(id=post_id)
    if new_post.author != request.user:
        messages.info(request,"Вы не являетесь автором поста!")
        return redirect('post_detail', post_id=post_id)
    if request.method == "POST":
        form = PostCreateForm(request.POST, request.FILES, instance=new_post)
        if form.is_valid():
            form.save()
            messages.success(request,"Пост успешно добавлен!")
            return redirect('home')
    else:
        form = PostCreateForm()

    context = {
        'form': form
    }
    return render(request, 'posts/update_post.html', context)

def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if post.author != request.user:
        messages.info(request, "Вы не являетесь автором поста!")
        return redirect('post_detail', post_id=post_id)
    if request.method == "POST":
        post.delete()
        messages.success(request, "Пост успешно удален!")
        return redirect('home')
    context = {
        'post': post
    }
    return render(request, 'posts/delete_post.html', context)