from django.test import TestCase
from django.urls import reverse
from .models import Testimonial
from django.contrib.auth.models import User


class TestimonialModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="password123"
            )
        self.testimonial = Testimonial.objects.create(
            user=self.user,
            title="Great Experience",
            content="I loved volunteering here!"
        )

    def test_testimonial_str(self):
        self.assertEqual(str(self.testimonial), "Great Experience")


class TestimonialViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="password123"
            )
        self.client.login(username="testuser", password="password123")

    def test_testimonial_list_view(self):
        response = self.client.get(reverse('testimonial_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'testimonials/testimonial_list.html')

    def test_add_testimonial_view(self):
        response = self.client.get(reverse('add_testimonial'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'testimonials/add_testimonial.html')
