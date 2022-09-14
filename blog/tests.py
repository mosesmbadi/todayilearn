from django.test import TestCase
from .models import Blog


class BlogModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Blog.objects.create(title='first blog')
        Blog.objects.create(body='a body here')

    def test_title_content(self):
        blog = Blog.objects.get(id=1)
        expected_object_name = f'{blog.title}'
        self.assertEquals(expected_object_name, 'first blog')

    def test_body_content(self):
        blog = Blog.objects.get(id=2)
        expected_object_name = f'{blog.body}'
        self.assertEquals(expected_object_name, 'a body here')
