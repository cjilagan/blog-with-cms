from django.shortcuts import render, get_object_or_404 
from django.core.paginator import Paginator
from .models import Post

def home(request):
    latest_posts = Post.objects.filter(status='published').order_by('-created_at')[:5]
    return render(request, 'posts/home.html', {'latest_posts': latest_posts})

def post_list(request):
    posts = Post.objects.filter(status='published').order_by('-created_at')
    paginator = Paginator(posts, 5)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'posts/post_list.html', {'page_obj': page_obj})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    return render(request, 'posts/post_detail.html', {'post': post})