from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Post, Category, Comment
from .forms import CommentForm


def home(request):
    """Home page view - TEAM MEMBER 3 RESPONSIBILITY"""
    latest_posts = Post.objects.filter(published=True)[:5]
    categories = Category.objects.all()
    
    context = {
        'latest_posts': latest_posts,
        'categories': categories,
    }
    return render(request, 'blog/home.html', context)


def post_list(request):
    """List all blog posts - TEAM MEMBER 3 RESPONSIBILITY"""
    posts = Post.objects.filter(published=True)
    categories = Category.objects.all()
    
    category_filter = request.GET.get('category')
    if category_filter:
        posts = posts.filter(category__name=category_filter)
    
    context = {
        'posts': posts,
        'categories': categories,
        'selected_category': category_filter,
    }
    return render(request, 'blog/post_list.html', context)


def post_detail(request, pk):
    """Single post detail view - TEAM MEMBER 3 RESPONSIBILITY"""
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.filter(approved=True)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, 'Comment added successfully!')
            return render(request, 'blog/post_detail.html', {
                'post': post,
                'comments': comments,
                'form': CommentForm(),
            })
    else:
        form = CommentForm()
    
    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }
    return render(request, 'blog/post_detail.html', context)


def category_posts(request, category_name):
    """Posts by category - TEAM MEMBER 3 RESPONSIBILITY"""
    category = get_object_or_404(Category, name=category_name)
    posts = Post.objects.filter(category=category, published=True)
    
    context = {
        'category': category,
        'posts': posts,
    }
    return render(request, 'blog/category_posts.html', context)
