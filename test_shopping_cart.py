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

        #Check when stock is less. See if ValueError is raised
        with self.assertRaises(ValueError):
            self.cart.add_item(self.productOne, 25)

    #Test removal of items from the shopping cart
    #Removed item quantities are added back to the stock count
    #If the requested removal makes the quantity zero, the item is removed entirely from the cart
    def test_remove_item(self):
        self.cart.add_item(self.productOne, 5)
        self.cart.remove_item(self.productOne, 3)
        self.assertEqual(self.cart.items[self.productOne], 2)

        #Initial stock:20, After adding to cart: 15, After removal: 15+3 = 18
        #Initial cart quantity: 5, After removal: 2
        self.assertEqual(self.productOne.stock, 18)

        #ValueError is raised when requested removal count is greater than the quantity available in the cart
        with self.assertRaises(ValueError):
            self.cart.remove_item(self.productOne, 90)

    def test_price(self):
        #Check if the dictionary of items (cart) is empty
        print(type(self.cart.items))
        print(not bool(self.cart.items))

        self.cart.add_item(self.productOne, 10)
        self.cart.add_item(self.productTwo, 14)
        self.assertEqual(self.cart.get_total_price(), 500)

if __name__ == "__main__":
    unittest.main()