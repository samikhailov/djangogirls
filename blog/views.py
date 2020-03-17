from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView


class PostListView(ListView):
    model = Post
    paginate_by = 5


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("-published_date")
    return render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post_detail.html", {"post": post})
