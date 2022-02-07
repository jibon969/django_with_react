from django.test import SimpleTestCase
from django.urls import resolve, reverse
from blog.views import (
    blog_view
)


class UrlTestCase(SimpleTestCase):

    # Test blog_view urls
    def test_blog_view_test(self):
        url = reverse('blog')
        self.assertAlmostEqual(resolve(url).func, blog_view)