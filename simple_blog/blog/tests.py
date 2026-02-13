from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Category, Post, Comment


class CategoryModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            name='Technology',
            description='Tech related posts'
        )

    def test_category_creation(self):
        self.assertEqual(self.category.name, 'Technology')
        self.assertTrue(Category.objects.filter(name='Technology').exists())
        self.assertEqual(str(self.category), 'Technology')


class PostModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

        self.category = Category.objects.create(name='Technology')

        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post content.',
            author=self.user,
            category=self.category,
            status='published'
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.author.username, 'testuser')
        self.assertEqual(self.post.status, 'published')
        self.assertIsNotNone(self.post.slug)
        self.assertEqual(str(self.post), 'Test Post')


class CommentModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='commentuser',
            password='testpass123'
        )

        self.category = Category.objects.create(name='Technology')

        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post content.',
            author=self.user,
            category=self.category,
            status='published'
        )

        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            content='This is a test comment.'
        )

    def test_comment_creation(self):
        self.assertEqual(self.comment.author.username, 'commentuser')
        self.assertEqual(self.comment.post, self.post)
        self.assertTrue(self.comment.approved)
        self.assertEqual(self.post.comments.count(), 1)


class ViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='viewuser',
            password='testpass123'
        )

        self.category = Category.objects.create(name='Technology')

        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post content.',
            author=self.user,
            category=self.category,
            status='published'
        )

    def test_home_view(self):
        response = self.client.get(reverse('blog:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

    def test_post_list_view(self):
        response = self.client.get(reverse('blog:post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

    def test_post_detail_view(self):
        response = self.client.get(
            reverse('blog:post_detail', kwargs={'pk': self.post.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

