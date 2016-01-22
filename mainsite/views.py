from django.shortcuts import render, get_object_or_404

from .models import Post


def index(request):
    return render(request=request, template_name='mainsite/index.html', context={'post_all': Post.objects.all()})


def post(request, post_id):
    post_object = get_object_or_404(Post, pk=post_id)
    return render(request=request, template_name='mainsite/post.html', context={'post_object': post_object})

