import logging
import random

import atoma
import requests
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO)


class Kempfolds(object):
    def __init__(self):
        """Constructor of KempfoldsSlackbot Class

        Attributes:
            kemp_images (list): Store kempfolds found from Atom entries
        """
        self.kemp_images = []

    def get_posts(self):
        """
        Retrieves posts from a Blogger blog using its Atom feed.

        Returns:
            An AtomFeed object representing the blog's feed data.

        Raises:
            Exception: An error occurred while fetching the posts.
        """
        url = "http://kempfolds.blogspot.com/feeds/posts/default"
        try:
            # Send a GET request to the specified URL
            response = requests.get(url)
            # Parse the response content as Atom feed data
            feed_data = atoma.parse_atom_bytes(response.content)
            # Return the parsed feed data
            return feed_data
        except requests.exceptions.RequestException as error:
            # If there is an error fetching the posts, raise an exception with the error message
            raise Exception(f"Error fetching posts: {error}")

    def return_kemps(self):
        """Parse the content of the Atom feed entries for KempfoldsSlackbot images, if found store each that is found"""
        feed = self.get_posts()
        entries = feed.entries

        for entry in entries:
            soup = BeautifulSoup(entry.content.value, features="html.parser")
            image = soup.find("img", src=True)
            if image:
                self.kemp_images.append(image["src"])

    @property
    def get_random_kemp(self):
        """
        Retrieves a random URL containing an image.

        Returns:
            kemp_image (item from list): A URL of a Kempfolds images.
        """
        return random.choice(self.kemp_images)


if __name__ == "__main__":
    kemp = Kempfolds()
    kemp.return_kemps()
    kemp_image = kemp.get_random_kemp
    logging.info(f"return_kemp succeeded: {kemp_image}")
    kemp_image
