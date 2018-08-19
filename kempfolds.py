import requests
import atoma
from bs4 import BeautifulSoup
import random


class Kempfolds(object):

    def __init__(self):
        """ Constructor of Kempfolds Class

        Attributes:
            response (Response): The requests response to Kempfolds Atom feed
            feed (AtomFeed): Parsed Atom XML using Atoma
            kemp_images (list): Store kempfolds found from Atom entries
        """
        self.response = requests.get("http://kempfolds.blogspot.com/feeds/posts/default")
        self.feed = atoma.parse_atom_bytes(self.response.content)
        self.kemp_images = []

    def return_kemps(self):
        """ Parse the content of the Atom feed entries for Kempfolds images, if found store each that is found

        Attributes:
            entries (list): List of AtomEntries, which hold a Kempfolds image.
        """
        self.entries = self.feed.entries

        for entry in self.entries:
            soup = BeautifulSoup(entry.content.value, features="html.parser")
            image = soup.find('img', src=True)
            if image:
                self.kemp_images.append(image['src'])

    @property
    def return_kemp(self):
        """ Select a random Kempfolds

        Returns:
            kemp_images (item from list): A random Kempfolds image
        """
        self.return_kemps()
        return random.choice(self.kemp_images)


if __name__ == "__main__":
    Kempfolds().return_kemp
