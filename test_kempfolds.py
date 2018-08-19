import unittest
import kempfolds as Kempfolds

class TestKempfolds(unittest.TestCase):
    """
    Tests for kempfolds module

    What to test:
        - NOT Atoma or it converting the data to ... something
            - This would potentially need a try, catch in the code to ensure the response has valid content
        - NOT BeautifulSoup, test that what Beautiful soup can pass to us can be used to get our result.

        -
    """
    kemp = Kempfolds() # Instantiate the Kempfolds Class
    kemp_image = [] # Variable that stores 'a' kempfold


if __name__ == "__main__":
    pass
