import requests
import atoma
from bs4 import BeautifulSoup
import random


class Kempfolds(object):

    def __init__(self):
        self.response = requests.get("http://kempfolds.blogspot.com/feeds/posts/default")
        self.feed = atoma.parse_atom_bytes(self.response.content)
        self.kemp_images = []

    @property
    def return_kemps(self):
        self.entries = self.feed.entries

        for entry in self.entries:
            soup = BeautifulSoup(entry.content.value, features="html.parser")
            image = soup.find('img', src=True)
            if image:
                self.kemp_images.append(image['src'])

    @property
    def return_kemp(self):
        self.return_kemps
        return random.choice(self.kemp_images)


kemp = Kempfolds()
print(kemp.return_kemp)