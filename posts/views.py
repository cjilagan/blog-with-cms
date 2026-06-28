from django.shortcuts import render, get_object_or_404 
from django.core.paginator import Paginator
from .models import Post, Category

def home(request):
    latest_posts = Post.objects.filter(status='published').order_by('-created_at')[:5]
    return render(request, 'posts/home.html', {'latest_posts': latest_posts})

def post_list(request):
    posts = Post.objects.filter(status='published').order_by('-created_at')
    
    category_slug = request.GET.get('category')
    if category_slug:
        posts = posts.filter(categories__slug=category_slug)
    
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    categories = Category.objects.all()
    
    return render(request, 'posts/post_list.html', {
        'page_obj': page_obj,
        'categories': categories,
        'current_category': category_slug,
    })

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    return render(request, 'posts/post_detail.html', {'post': post})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(categories=category, status='published').order_by('-created_at')
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'posts/category_detail.html', {
        'category': category,
        'page_obj': page_obj,
    })

def search(request):
    query = request.GET.get('q', '')
    results = Post.objects.filter(
        status='published',
        title__icontains=query
    ).order_by('-created_at') if query else Post.objects.none()
    return render(request, 'posts/search.html', {
        'results': results,
        'query': query,
    })