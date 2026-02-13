from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),

    path('posts/', views.post_list, name='post_list'),

    # SEO-friendly slug URL
    path('posts/<slug:slug>/', views.post_detail, name='post_detail'),

    # Better structured category URL
    path('category/<slug:category_name>/', views.category_posts, name='category_posts'),
]
