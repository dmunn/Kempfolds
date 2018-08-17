import requests
import atoma
from bs4 import BeautifulSoup
import random


class Kempfolds(object):

    def __init__(self):
        """ Constructor of KempfoldsSlackbot Class

        Attributes:
            kemp_images (list): Store kempfolds found from Atom entries
        """
        self.kemp_images = []

    def get_posts(self):
        try:
            response = requests.get("http://kempfolds.blogspot.com/feeds/posts/default")
            feed = atoma.parse_atom_bytes(response.content)
            return feed
        except requests.exceptions.RequestException as e:
            print(e)

    def return_kemps(self):
        """ Parse the content of the Atom feed entries for KempfoldsSlackbot images, if found store each that is found

        """
        feed = self.get_posts()
        entries = feed.entries

        for entry in entries:
            soup = BeautifulSoup(entry.content.value, features="html.parser")
            image = soup.find('img', src=True)
            if image:
                self.kemp_images.append(image['src'])

    @property
    def return_kemp(self):
        """ Select a random KempfoldsSlackbot

        Returns:`
            kemp_images (item from list): A random KempfoldsSlackbot image
        """
        self.return_kemps()
        return random.choice(self.kemp_images)


if __name__ == "__main__":
    Kempfolds().return_kemp
