from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Prefetch
from .models import Post, Category, Comment
from .forms import CommentForm


def home(request):
    """Home page view"""

    latest_posts = (
        Post.objects
        .filter(status='published')
        .select_related('author', 'category')
        .order_by('-created_date')[:5]
    )

    categories = Category.objects.all()

    return render(request, 'blog/home.html', {
        'latest_posts': latest_posts,
        'categories': categories,
    })


def post_list(request):
    """List all blog posts"""

    posts = (
        Post.objects
        .filter(status='published')
        .select_related('author', 'category')
        .order_by('-created_date')
    )

    categories = Category.objects.all()

    category_filter = request.GET.get('category')

    if category_filter:
        posts = posts.filter(category__name=category_filter)

    return render(request, 'blog/post_list.html', {
        'posts': posts,
        'categories': categories,
        'selected_category': category_filter,
    })


def post_detail(request, slug):
    """Single post detail view"""

    post = get_object_or_404(
        Post.objects.select_related('author', 'category'),
        slug=slug,
        status='published'
    )

    comments = post.comments.filter(approved=True)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post

            # If comments require login
            if request.user.is_authenticated:
                comment.author = request.user

            comment.save()
            messages.success(request, 'Comment added successfully!')
            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form,
    })


def category_posts(request, category_name):
    """Posts by category"""

    category = get_object_or_404(Category, name=category_name)

    posts = (
        Post.objects
        .filter(category=category, status='published')
        .select_related('author')
        .order_by('-created_date')
    )

    return render(request, 'blog/category_posts.html', {
        'category': category,
        'posts': posts,
    })
