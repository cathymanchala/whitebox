from givencode import Product, ShoppingCart, Customer, PaymentGateway
import unittest

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        #Product: name, price, stock
        self.productOne = Product("TestProductOne", 15,20)
        self.productTwo = Product("TestProductTwo", 25, 40)
        self.productThree = Product("Coffee", 10, 40)
        self.cart = ShoppingCart()
    
    def test_add_item(self):
        self.cart.add_item(self.productOne, 4)

        #Check if the quantity of the item in the shopping cart is matched
        self.assertEqual(self.cart.items[self.productOne], 4)

        #Check if the stock of the item is matched after adding to cart
        self.assertEqual(self.productOne.stock, 16)

        #Check when stock is less. See if ValueError is raised.
        with self.assertRaises(ValueError):
            self.cart.add_item(self.productOne, 25)


if __name__ == "__main__":
    unittest.main()