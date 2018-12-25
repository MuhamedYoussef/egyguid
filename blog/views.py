from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404


def blog(request):
    context = {
        'posts': Post.objects.order_by('id')
    }
    return render(request, 'blog/blog.html', context)


def post(request, slug):
    context = {
        'post': get_object_or_404(Post, slug=slug)
    }
    return render(request, 'blog/post.html', context)
