from django.contrib import admin
from .models import Category, Post, Comment


class CommentInline(admin.TabularInline):
    """Inline comments for posts."""
    model = Comment
    extra = 0
    fields = ['author', 'content', 'approved', 'created_date']
    readonly_fields = ['created_date']
    ordering = ['-created_date']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Category admin - TEAM MEMBER 2 RESPONSIBILITY"""
    list_display = ['name', 'created_date', 'post_count']
    search_fields = ['name']
    ordering = ['name']
    
    def post_count(self, obj):
        """Display number of posts in category."""
        return obj.post_set.count()
    post_count.short_description = 'Posts'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin - TEAM MEMBER 2 RESPONSIBILITY"""
    list_display = ['title', 'author', 'category', 'published', 'created_date', 'comment_count']
    list_filter = ['published', 'created_date', 'category']
    search_fields = ['title', 'content', 'author__username']
    list_editable = ['published']
    date_hierarchy = 'created_date'
    ordering = ['-created_date']
    inlines = [CommentInline]
    
    def comment_count(self, obj):
        """Display number of comments on post."""
        return obj.comment_set.count()
    comment_count.short_description = 'Comments'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Comment admin - TEAM MEMBER 3 RESPONSIBILITY"""
    list_display = ['author', 'post_link', 'approved', 'created_date']
    list_filter = ['approved', 'created_date']
    search_fields = ['author', 'content']
    list_editable = ['approved']
    readonly_fields = ['created_date']
    ordering = ['-created_date']
    
    def post_link(self, obj):
        """Link to parent post."""
        return obj.post.title
    post_link.short_description = 'Post'
    post_link.admin_order_field = 'post__title'
