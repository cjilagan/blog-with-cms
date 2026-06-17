from django.shortcuts import render, get_object_or_404 
from .models import Post

def home(request):
    latest_posts = Post.objects.filter(status='published').order_by('-created_at')[:5]
    return render(request, 'posts/home.html', {'latest_posts': latest_posts})

def post_list(request):
    posts = Post.objects.filter(status='published')
    return render(request, 'posts/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    return render(request, 'posts/post_detail.html', {'post': post})