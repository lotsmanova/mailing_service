from django.http import Http404
from django.shortcuts import get_object_or_404
from django.test import TestCase
from django.urls import reverse

from blog.models import Blog


class BlogTestCase(TestCase):
    def setUp(self):
        self.blog = Blog.objects.create(
            head='Test',
            body='Test'
        )

    def test_create_blog(self):
        """Тестирование создание блога"""
        data = {
            'head': 'Test_create',
            'body': 'Test_create'
        }

        response = self.client.post(
            reverse('blog:blog_create'),
            data=data
        )

        blog = Blog.objects.get(head='Test_create')

        self.assertEqual(blog.body, 'Test_create')


    def test_list_blog(self):
        """Тестирование вывода списка блога"""

        response = self.client.get(reverse('blog:blog_list'))

        self.assertEqual(response.status_code, 200)


    def test_detail_blog(self):
        """Тестирование вывода блога"""

        response = self.client.get(reverse('blog:blog_detail', kwargs={'pk': self.blog.id}))

        self.assertEqual(response.status_code, 200)


    def test_update_blog(self):
        """Тестирование обновления блога"""

        response = self.client.post(
            reverse('blog:blog_update', kwargs={'pk': self.blog.id}),
            {'id': 1, 'head': 'test update', 'body': 'test update'}
        )

        update_blog = Blog.objects.get(head='test update')

        self.assertEqual(update_blog.body, 'test update')


    def test_delete_blog(self):
        """Тестирование удаления блога"""

        response = self.client.delete(
            reverse('blog:blog_delete', kwargs={'pk': self.blog.id})
        )

        with self.assertRaises(Http404):
            get_object_or_404(Blog, head='Test')
