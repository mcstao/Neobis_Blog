from django.shortcuts import render, redirect


from post_app.forms import PostCreateForm
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


def add_post(request):
    if request.method == "POST":
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostCreateForm()

    context = {
        'form': form
    }
    return render(request, 'posts/add_post.html', context)

def update_post(request, post_id):
    new_post = Post.objects.get(id=post_id)
    if request.method == "POST":
        form = PostCreateForm(request.POST, request.FILES, instance=new_post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostCreateForm()

    context = {
        'form': form
    }
    return render(request, 'posts/update_post.html', context)