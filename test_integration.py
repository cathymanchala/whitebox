from shop import Product, ShoppingCart, Customer, PaymentGateway
import unittest

class TestShopIntegration(unittest.TestCase):
     
    def setUp(self):
        self.customer = Customer("Tim")
        self.customerTwo = Customer("Edward")

        #Add products to stock
        self.productOne = Product("Espresso", 30, 50)
        self.productTwo = Product("Mocha", 35, 50)
        self.productThree = Product("Soda", 10.5, 20)
        
    def test_cart_operations(self):
        self.customer.cart.add_item(self.productOne, 3)
        self.customer.cart.add_item(self.productTwo, 5)
        self.customer.cart.add_item(self.productThree, 9)

        self.customer.cart.remove_item(self.productOne, 1)
        self.customer.cart.remove_item(self.productTwo, 2)
        
        #Compare the manually calculated cart value to the returned value from get_total_price() method
        cartValue = 0
        for product, quantity in self.customer.cart.items.items():
            cartValue += (product.price * quantity)

        self.assertEqual(cartValue, self.customer.cart.get_total_price())

        #Verify product quantities from cart and stock
        self.assertEqual(self.customer.cart.items[self.productOne], 2)
        self.assertEqual(self.customer.cart.items[self.productTwo], 3)
        self.assertEqual(self.customer.cart.items[self.productThree], 9)

        self.assertEqual(self.productOne.stock, 48)
        self.assertEqual(self.productTwo.stock, 47)
        self.assertEqual(self.productThree.stock, 11)

        self.customer.checkout()

        #Add an item with insufficient stock
        with self.assertRaises(ValueError):
            self.customer.cart.add_item(self.productOne, 100)

        #Remove an item which is not present in the cart
        #'productFour' does not exist
        with self.assertRaises(AttributeError):
            self.customer.cart.remove_item(self.productFour, 10)
        
        #Checking out with an empty cart
        self.customerTwo.checkout()
    
if __name__ == "__main__":
    unittest.main()