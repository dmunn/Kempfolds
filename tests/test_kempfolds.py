import unittest
import responses
from unittest.mock import patch

from .mock_data import response_content
from Kempfolds.Kempfolds import Kempfolds


class TestKempfolds(unittest.TestCase):

    # Example 1 - Test a mocked response body I created. Is this worth it, please let me know?
    def test_kempfolds_response_is_not_empty(self):
        """
        Test getting content from our Blog
        """
        response = response_content
        # Check the content is not empty
        self.assertIsNotNone(response)

    # Test a mocked Kempfolds class's content for type checking... or so I thought
    @patch('Kempfolds.Kempfolds')
    def test_kempfolds_response_is_of_type_bytes(self, MockBlog):
        blog_response = response_content

        self.assertEqual(type(blog_response), bytes)

    # Use responses to mock the responses body and content_type
    @responses.activate
    def test_kempfolds_get_posts_is_of_valid_type(self):
        """
        Test that we have at least one blog entry once it's parsed by Atoma.
        Create the mocked response using responses and then call the the get_posts method which will use the mocked response
        instead of calling out to the real life URL for a response.
        """
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
