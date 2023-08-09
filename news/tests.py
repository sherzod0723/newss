from django.test import TestCase
from django.urls import reverse
from .models import  Post
# Create your tests here.


class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(title='Mavzu', text='Yangiliklar matni')

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_title = f'{post.title}'
        expected_object_text = f'{post.text}'
        self.assertEquals(expected_object_title, 'Mavzu')
        self.assertEquals(expected_object_text, 'Yangiliklar matni')



class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(title='Mavzu 2', text=' Yangiliklar matni')

    def test_views_urls_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEquals(resp.status_code, 200)

    def test_view_user_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEquals(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
