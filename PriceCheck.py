from typing import List
import unittest

def priceCheck(products: List[str], productPrices: List[float], productSold: List[str], soldPrice: List[float]) -> int:
    """
    products: list of product names
    productPrices: list of prices for each product
    productSold: list of product names sold
    soldPrice: list of prices for each product sold
    return: number of products with incorrect price
    """
    # assert len(products) == len(productPrices)
    # assert len(productSold) == len(soldPrice)
    # assert isinstance(products, list) and all(isinstance(i, str) for i in products)
    # assert isinstance(productPrices, list) and all(isinstance(i, str) for i in productPrices)
    # assert isinstance(productSold, list) and all(isinstance(i, str) for i in productSold)
    # assert isinstance(soldPrice, list) and all(isinstance(i, float) for i in soldPrice)
    error_count = 0
    product_prices = dict(zip(products, productPrices))
    for i in range(len(productSold)):
        if product_prices.get(productSold[i], None) != soldPrice[i]:
            error_count += 1
    return error_count

# tests:

class MyTests(unittest.TestCase):

    def test_priceCheck(self):
        products = ['apple', 'orange', 'lemon', 'banana']
        productPrices = [16.89, 56.92, 20.89, 345.99]
        productSold = ['apple', 'banana']
        soldPrice = [16.89, 345.99]
        self.assertEqual(priceCheck(products, productPrices, productSold, soldPrice), 0)

    def test_priceCheck_errors(self):
        products = ['apple', 'banana', 'orange', 'lemon']
        productPrices = [16.89, 56.92, 20.89, 345.99]
        productSold = ['apple', 'lemon']
        soldPrice = [18.99, 400.89]
        self.assertEqual(priceCheck(products, productPrices, productSold, soldPrice), 2)

    def test_priceCheck_no_product(self):
        products = ['apple', 'banana', 'orange', 'lemon']
        productPrices = [16.89, 56.92, 20.89, 345.99]
        productSold = ['strawberry', 'lemon']
        soldPrice = [18.99, 400.89]
        self.assertEqual(priceCheck(products, productPrices, productSold, soldPrice), 2)
        

if __name__ == '__main__':
    unittest.main()
