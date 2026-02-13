from django.db import models
from django.utils import timezone


class Category(models.Model):
    """Blog category model - TEAM MEMBER 2 RESPONSIBILITY Sumesh"""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Post(models.Model):
    """Blog post model - TEAM MEMBER 2 RESPONSIBILITY"""
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    """Comment model - TEAM MEMBER 3 RESPONSIBILITY"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['created_date']
    
    def __str__(self):
        return f'Comment by {self.author} on {self.post.title}'
