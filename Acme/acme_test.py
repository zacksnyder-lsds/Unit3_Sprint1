import unittest
from acme import Product
from acme_report import generate_products, adjective, noun

class AcmeProductTests(unittest.TestCase):
    ''' Making Sure Acme products are the tops!'''
    def test_default_product_price(self):
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_weight(self):
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_explode(self): 
        prod = Product('Test Product', weight=50)
        self.assertEqual(prod.explode(), '...Boom!')

class AcmeReportTests(unittest.TestCase):
    '''Testing Functionality of reports generator'''
    def test_default_num_products(self):
        self.assertEqual(len(generate_products()), 30)

    def test_legal_names(self):
        name = generate_products()[1][1]
        for nouns in noun:
            self.assertIn(name, nouns)
        for adjectives in adjective:
            self.assertIn(name, adjectives)
        self.assertIn('', name)

if __name__ == '__main__':
    unittest.main()