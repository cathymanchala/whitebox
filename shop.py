class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, product, quantity):
        if quantity > 0 and product.stock >= quantity:
            if product in self.items:
                self.items[product] += quantity
            else:
                self.items[product] = quantity
            product.stock -= quantity
        else:
            raise ValueError("Invalid quantity or insufficient stock")

    def remove_item(self, product, quantity):
        if product in self.items and quantity > 0 and quantity <= self.items[product]:
            self.items[product] -= quantity
            product.stock += quantity
            if self.items[product] == 0:
                del self.items[product]
        else:
            raise ValueError("Invalid quantity or item not found")  

    def get_total_price(self):
        total_price = 0
        for product, quantity in self.items.items():
            total_price += product.price * quantity
        return total_price


class PaymentGateway:
    @staticmethod
    def process_payment(customer, total_amount):
        # Simulate a payment process (not real payment)
        print(f"Processing payment of ${total_amount:.2f} for {customer.name}")
        return True

class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = ShoppingCart()

    def checkout(self):
        # Simulate a checkout process
        total_price = self.cart.get_total_price()
        print("t", total_price)
        if total_price > 0:
            payment_successful = PaymentGateway.process_payment(self, total_price)
            if payment_successful:
                print(f"Payment successful! Thank you, {self.name}!")
                # In a real system, you'd update the order and handle shipping, etc.
            else:
                print ("Payment failed. Please try again.")
        else:
            print ("No items in the cart.")