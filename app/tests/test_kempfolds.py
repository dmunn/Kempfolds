from unittest.mock import patch

import atoma
import pytest
import requests
from app.Kempfolds.Kempfolds import Kempfolds


class TestKempImages:
    def setup_method(self, method):
        self.instance = Kempfolds()
        self.kemp_images = [
            "https://example.com/image1.jpg",
            "https://example.com/image2.jpg",
        ]

    def test_get_random_kemp_positive(self):
        # Define the expected return value
        expected_value = "path/to/kemp/image.jpg"

        # Mock the get_random_kemp() method to return the expected value
        with patch("app.Kempfolds.Kempfolds.get_random_kemp") as mock_method:
            mock_method.return_value = expected_value

            # Call the method under test
            kemp_image = self.instance.get_random_kemp()

            # Assert that the method returned the expected value
            assert kemp_image == expected_value

    def test_get_random_kemp_negative(self):
        self.kemp_images = []
        with pytest.raises(IndexError):
            self.instance.get_random_kemp()

    def test_get_posts_success(self):
        with patch("requests.get") as mock_request:
            mock_response = requests.Response()
            mock_response.status_code = 200
            mock_response._content = b"""<?xml version="1.0" encoding="UTF-8"?>
            <feed xmlns="http://www.w3.org/2005/Atom" xml:lang="en">
            <id>urn:uuid:60a76c80-0a78-11ec-9a03-0242ac130003</id>
            <title>Example Feed</title>
            <updated>2021-09-02T14:25:00Z</updated>
            <entry>
                <id>urn:uuid:60a76c80-0a78-11ec-9a03-0242ac130004</id>
                <title>Example Entry</title>
                <updated>2021-09-02T14:25:00Z</updated>
                <author>
                <name>John Doe</name>
                <email>john.doe@example.com</email>
                </author>
                <content type="html">This is an example entry.</content>
            </entry>
            </feed>"""
            mock_request.return_value = mock_response
            my_class = Kempfolds()
            feed_data = my_class.get_posts()
            assert isinstance(feed_data, atoma.atom.AtomFeed)

    def test_get_posts_failure(self):
        with patch("requests.get") as mock_request:
            mock_request.side_effect = requests.exceptions.RequestException()
            my_class = Kempfolds()
            with pytest.raises(Exception):
                my_class.get_posts()


if __name__ == "__main__":
    tests = TestKempImages()
    tests
