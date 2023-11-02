from django.shortcuts import render


from post_app.models import Post


def home(request):
    if request.method == "GET":
        posts = Post.objects.all()
        context = {
            'posts': posts
        }
        return render(request, 'posts/home.html', context)

