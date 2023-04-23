import random  # importing random library

class Product:  # main class for product information
    def __init__(self, name, price, attributes):
        self.name = name
        self.price = price
        self.attributes = attributes

class Cart:  # a class for cart information
    def __init__(self):
        self.items = []  # The cart list

    def add_item(self, product, quantity, attributes):
        self.items.append({'product': product, 'quantity': quantity, 'attributes': attributes})

    def remove_item(self, item):
        self.items.remove(item)

    def get_total_price(self):
        total_price = 0
        for item in self.items:
            total_price += item['product'].price * item['quantity']
        return total_price
    
class Order:  # class for order information and payment
    def __init__(self, cart, address, phone_number, name, delivery_time, delivery_method):
        self.cart = cart
        self.address = address
        self.phone_number = phone_number
        self.name = name
        self.delivery_time = delivery_time
        self.delivery_method = delivery_method
        self.order_number = random.randint(10000000000, 99999999999)  # using random library