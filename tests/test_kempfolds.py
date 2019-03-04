import unittest
import responses
from unittest.mock import patch

from .mock_data import response_content
from Kempfolds.Kempfolds import Kempfolds


class TestKempfolds(unittest.TestCase):

    @patch('Kempfolds.Kempfolds')
    def test_kempfolds_response_is_not_empty(self, MockBlog):
        blog_response = response_content

        self.assertIsNotNone(blog_response)

    @patch('Kempfolds.Kempfolds')
    def test_kempfolds_response_is_of_type_bytes(self, MockBlog):
        blog_response = response_content

        self.assertEqual(type(blog_response), bytes)

    @responses.activate
    def test_kempfolds_get_posts_is_of_valid_type(self):
        responses.add(
            responses.GET,
            "http://kempfolds.blogspot.com/feeds/posts/default",
            body=response_content,
            content_type="application/json"
        )

        MockBlog = Kempfolds()
        response = MockBlog.get_posts()
        self.assertTrue(len(response.entries) > 0, "Ensure there is at least one entry in our returned Atom feed")


if __name__ == "__main__":
    TestKempfolds()
