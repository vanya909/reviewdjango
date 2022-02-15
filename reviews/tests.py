from django.test import TestCase
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

from .models import Review, Site


class TestDetail(TestCase):

    def setUp(self):
        self.test_user = self.create_test_user()
        self.test_site = self.create_test_site()
        self.test_review = self.create_test_review(self.test_site, self.test_user)

    def test_detail_page_status_code(self):
        response = self.client.get(f'/reviews/{self.test_review.pk}')
        self.assertEqual(response.status_code, 200, "Detail page code isn't 200")

    def test_detail_page_reverse_lazy_status_code(self):
        response_reverse_lazy = self.client.get(reverse_lazy('review_detail', args=[self.test_review.pk, ]))
        self.assertEqual(response_reverse_lazy.status_code, 200, "Detail page reverse lazy code isn't 200")

    def test_detail_page_template(self):
        response = self.client.get(reverse_lazy('review_detail', args=[self.test_review.pk,]))
        self.assertTemplateUsed(response, 'reviews/detail.html', "Detail template isn't reviews/detail.html")

    def create_test_user(self):
        return get_user_model().objects.create_user('login', 'email@mail.com', 'password')

    def create_test_site(self):
        site = Site(domain_name='google', domain='com')
        site.save()
        return site

    def create_test_review(self, site, author):
        review = Review(site=site, rating=5, description='description', author=author)
        review.save()
        return review


class TestList(TestCase):

    def test_list_page_status_code(self):
        response = self.client.get('/reviews/list/')
        self.assertEqual(response.status_code, 200, "List page code isn't 200")

    def test_list_page_reverse_lazy_status_code(self):
        response_reverse_lazy = self.client.get(reverse_lazy('review_list'))
        self.assertEqual(response_reverse_lazy.status_code, 200, "List page reverse lazy code isn't 200")

    def test_list_page_template(self):
        response = self.client.get(reverse_lazy('review_list'))
        self.assertTemplateUsed(response, 'reviews/list.html', "List template isn't reviews/list.html")
