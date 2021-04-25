import unittest
from page_objects.main import Amazon


class Am(unittest.TestCase):
    def setUp(self):
        self.web = Amazon()
        self.web.load_ama_page()

    def test_try_to_test(self):
        self.web.search_products()
        self.web.buy_now()

    def tearDown(self):
        self.web.close_page()


if __name__ == '__main__':
    unittest.main()
