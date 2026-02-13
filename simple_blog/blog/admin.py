from django.contrib import admin
from .models import Category, Post, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Category admin - TEAM MEMBER 2 RESPONSIBILITY"""
    list_display = ['name', 'created_date']
    search_fields = ['name']
    ordering = ['name']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin - TEAM MEMBER 2 RESPONSIBILITY"""
    list_display = ['title', 'author', 'category', 'published', 'created_date']
    list_filter = ['published', 'created_date', 'category']
    search_fields = ['title', 'content', 'author']
    list_editable = ['published']
    date_hierarchy = 'created_date'
    ordering = ['-created_date']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Comment admin - TEAM MEMBER 3 RESPONSIBILITY"""
    list_display = ['author', 'post', 'approved', 'created_date']
    list_filter = ['approved', 'created_date']
    search_fields = ['author', 'content']
    list_editable = ['approved']
    ordering = ['-created_date']
