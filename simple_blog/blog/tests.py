from django.test import TestCase
from django.urls import reverse
from .models import Category, Post, Comment


class CategoryModelTest(TestCase):
    """Test cases for Category model - TEAM MEMBER 2 RESPONSIBILITY"""
    
    def setUp(self):
        self.category = Category.objects.create(
            name='Technology',
            description='Tech related posts'
        )
    
    def test_category_creation(self):
        """Test category creation"""
        self.assertEqual(self.category.name, 'Technology')
        self.assertEqual(str(self.category), 'Technology')


class PostModelTest(TestCase):
    """Test cases for Post model - TEAM MEMBER 2 RESPONSIBILITY"""
    
    def setUp(self):
        self.category = Category.objects.create(name='Technology')
        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post content.',
            author='Test Author',
            category=self.category
        )
    
    def test_post_creation(self):
        """Test post creation"""
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.author, 'Test Author')
        self.assertEqual(str(self.post), 'Test Post')


class CommentModelTest(TestCase):
    """Test cases for Comment model - TEAM MEMBER 3 RESPONSIBILITY"""
    
    def setUp(self):
        self.category = Category.objects.create(name='Technology')
        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post content.',
            author='Test Author',
            category=self.category
        )
        self.comment = Comment.objects.create(
            post=self.post,
            author='Comment Author',
            content='This is a test comment.'
        )
    
    def test_comment_creation(self):
        """Test comment creation"""
        self.assertEqual(self.comment.author, 'Comment Author')
        self.assertEqual(self.comment.post, self.post)
        self.assertTrue(self.comment.approved)


class ViewTest(TestCase):
    """Test cases for views - TEAM MEMBER 3 RESPONSIBILITY"""
    
    def setUp(self):
        self.category = Category.objects.create(name='Technology')
        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post content.',
            author='Test Author',
            category=self.category
        )
    
    def test_home_view(self):
        """Test home page"""
        response = self.client.get(reverse('blog:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
    
    def test_post_list_view(self):
        """Test post list page"""
        response = self.client.get(reverse('blog:post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
    
    def test_post_detail_view(self):
        """Test post detail page"""
        response = self.client.get(reverse('blog:post_detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
