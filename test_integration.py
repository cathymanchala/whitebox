from givencode import Product, ShoppingCart, Customer, PaymentGateway
import unittest

class TestShopIntegration(unittest.TestCase):
     
     #Setup for the required entities: Products, customer and cart.

    def setUp(self):

        self.customer = Customer("Tim")

        #Add products to stock
        self.productOne = Product("Espresso", 30, 50)
        self.productTwo = Product("Mocha", 35, 50)
        

    #Test addition and deletion of items to the cart

    def test_cart_operations(self):
        self.customer.cart.add_item(self.productOne, 3)
        self.customer.cart.add_item(self.productTwo, 5)

        self.customer.cart.remove_item(self.productOne, 1)
        self.customer.cart.remove_item(self.productTwo, 2)
        
        #Compare the manually calculated cart value to the returned value from get_total_price() method.
        cartValue = 0
        for product, quantity in self.customer.cart.items.items():
            cartValue += (product.price * quantity)

        self.assertEqual(cartValue, self.customer.cart.get_total_price())

        #Verify product quantities from cart and stock
        #Cart: 2,3
        #Stock: 50-2 = 48, 50-3 = 47
        self.assertEqual(self.customer.cart.items[self.productOne], 2)
        self.assertEqual(self.customer.cart.items[self.productTwo], 3)

        self.assertEqual(self.productOne.stock, 48)
        self.assertEqual(self.productTwo.stock, 47)

        self.customer.checkout()
    
if __name__ == "__main__":
    unittest.main()