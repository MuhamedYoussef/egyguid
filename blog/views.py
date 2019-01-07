from django.shortcuts import render, redirect
from .models import Post
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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


@login_required
def add(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        url = request.POST['url']
        img = request.POST['img']

        if (url is None or url.strip() == '') and (img is None or img.strip() == ''):
            messages.error(request, 'Please provide an image')
            return redirect('add')

        post = Post.objects.create(
            owner=request.user,
            title=title,
            content=content,
            image_url=url,
            image=img
        )

        post.save()

        return redirect('blog')
    else:
        return render(request, 'blog/add.html')
