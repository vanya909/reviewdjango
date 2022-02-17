from django.test import TestCase
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

from .models import Review, Site


def create_test_user(username, email, password):
    """A function which creates user in the test model"""

    return get_user_model().objects.create_user(username, email, password)


def create_test_site(domain):
    """A function which creates site in the test model"""

    site = Site(domain=domain)
    site.save()
    return site


def create_test_review(site, author):
    """A function which creates review in the test model"""

    review = Review(site=site, rating=5, description='description', author=author)
    review.save()
    return review


class TestDetail(TestCase):

    def setUp(self):
        """Create a review to test"""

        self.test_user = create_test_user('username', 'email@email.com', 'password')
        self.test_site = create_test_site('google.com')
        self.test_review = create_test_review(self.test_site, self.test_user)

    def test_detail_page_status_code(self):
        """Check review detail page status code"""

        response = self.client.get(f'/reviews/{self.test_review.pk}')
        self.assertEqual(response.status_code, 200, "Detail page code isn't 200")

        response = self.client.get(f'/reviews/{self.test_review.pk + 1}')
        self.assertEqual(response.status_code, 404)

    def test_detail_page_reverse_lazy_status_code(self):
        """Check review detail page status code using reverse_lazy()"""

        response_reverse_lazy = self.client.get(reverse_lazy('review_detail', args=[self.test_review.pk, ]))
        self.assertEqual(response_reverse_lazy.status_code, 200, "Detail page reverse lazy code isn't 200")

    def test_detail_page_template(self):
        """Check whether the template is reviews/detail.html or not"""

        response = self.client.get(reverse_lazy('review_detail', args=[self.test_review.pk, ]))
        self.assertTemplateUsed(response, 'reviews/detail.html', "Detail template isn't reviews/detail.html")


class TestList(TestCase):
    """Test review list page"""

    def test_list_page_status_code(self):
        """Check review list page status code"""

        response = self.client.get('/reviews/list/')
        self.assertEqual(response.status_code, 200, "List page code isn't 200")

    def test_list_page_reverse_lazy_status_code(self):
        """Check review list page status code using reverse_lazy()"""

        response_reverse_lazy = self.client.get(reverse_lazy('review_list'))
        self.assertEqual(response_reverse_lazy.status_code, 200, "List page reverse lazy code isn't 200")

    def test_list_page_template(self):
        """Check whether the template is reviews/list.html or not"""

        response = self.client.get(reverse_lazy('review_list'))
        self.assertTemplateUsed(response, 'reviews/list.html', "List template isn't reviews/list.html")


class TestCreate(TestCase):
    """Test review creation page"""

    def setUp(self):
        """
        Create a user which need to be logged-in to test
        that only logged-in users can create a review
        """

        self.user_data = {
            'username': 'user',
            'email': 'email@email.com',
            'password': 'very_strong_password',
        }
        self.user = create_test_user(
            self.user_data['username'],
            self.user_data['email'],
            self.user_data['password'],
        )

    def test_create_page_status_code(self):
        """
        Check review creation page status code
        without user logged-in first and with user logged-in then
        """

        response = self.client.get('/reviews/create/')
        self.assertEqual(response.status_code, 302)

        self.client.login(
            username=self.user_data['username'],
            password=self.user_data['password'],
        )

        response = self.client.get('/reviews/create/')
        self.assertEqual(response.status_code, 200)

    def test_create_page_reverse_lazy_status_code(self):
        """
        Check review creation page status code using reverse_lazy()
        without user logged-in first and with user logged-in then
        """

        response = self.client.get(reverse_lazy('review_create'))
        self.assertEqual(response.status_code, 302)

        self.client.login(
            username=self.user_data['username'],
            password=self.user_data['password'],
        )

        response = self.client.get(reverse_lazy('review_create'))
        self.assertEqual(response.status_code, 200)

    def test_create_page_template(self):
        """Check whether the template is reviews/create.html or not"""

        self.client.login(
            username=self.user_data['username'],
            password=self.user_data['password'],
        )
        response = self.client.get(reverse_lazy('review_create'))
        self.assertTemplateUsed(response, 'reviews/create.html')


class TestDelete(TestCase):
    """Testing review delete page"""

    def setUp(self):
        """Creating user, site and review which we want to test"""

        self.user_data = {
            'username': 'user',
            'email': 'email@email.com',
            'password': 'very_strong_password',
        }
        self.test_user = create_test_user(
            self.user_data['username'],
            self.user_data['email'],
            self.user_data['password'],
        )
        self.test_site = create_test_site('google.com')
        self.test_review = create_test_review(self.test_site, self.test_user)

    def test_delete_page_status_code(self):
        """
        Check review delete page status code
        without user logged-in first and with user logged-in then
        """

        response = self.client.get(f'/reviews/{self.test_review.pk}/delete/')
        self.assertEqual(response.status_code, 403)

        self.client.login(
            username=self.user_data['username'],
            password=self.user_data['password']
        )

        response = self.client.get(f'/reviews/{self.test_review.pk}/delete/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get(f'/reviews/{self.test_review.pk + 1}/delete/')
        self.assertEqual(response.status_code, 404)

    def test_delete_page_reverse_lazy_status_code(self):
        """
        Check review delete page status code using reverse_lazy()
        without user logged-in first and with user logged-in then
        """

        response = self.client.get(reverse_lazy('review_delete', args=[self.test_review.pk, ]))
        self.assertEqual(response.status_code, 403)

        self.client.login(
            username=self.user_data['username'],
            password=self.user_data['password']
        )

        response = self.client.get(reverse_lazy('review_delete', args=[self.test_review.pk, ]))
        self.assertEqual(response.status_code, 200)

    def test_delete_page_template(self):
        """Check whether the template is reviews/delete.html or not"""

        self.client.login(
            username=self.user_data['username'],
            password=self.user_data['password']
        )
        response = self.client.get(reverse_lazy('review_delete', args=[self.test_review.pk, ]))
        self.assertTemplateUsed(response, 'reviews/delete.html')
