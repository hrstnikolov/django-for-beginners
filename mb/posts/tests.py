from cgitb import reset
from turtle import pos
from django.test import TestCase
from django.urls import reverse
from .models import Post


class PostModelTest(TestCase):
    def setUp(self) -> None:
        Post.objects.create(text='test post')
    
    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_text = post.text
        self.assertEqual(expected_text, 'test post')


class HomePageViewTest(TestCase):
    def setUp(self) -> None:
        Post.objects.create(text='simple text for testing')
    
    def test_view_url_exists_at_proper_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
