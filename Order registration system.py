import random  # importing random library

from Logistic_system import Address  # useing Logistic_system module

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
    def __init__(self, cart, address, phone_number, name):
        self.cart = cart
        self.address = address
        self.phone_number = phone_number
        self.name = name
        self.delivery_time = Address().choose_delivery_time() # functions from Logistic system
        self.delivery_method = Address().delivery_method()  # functions from Logistic system
        self.order_number = random.randint(10000000000, 99999999999)  # using random library
        
    def checkout(self, card_number):
        if len(str(card_number)) == 16:  # verifying card number
        # Payment successful
            with open('confirmation.txt', 'w') as f:  # creat and write in a txt file
                f.write(f'Card number: {card_number}\nStatus: Payment successful\nName: {self.name}')
            with open('invoice.txt', 'w') as f:
                f.write(f'Order number: {self.order_number}\nName: {self.name}\nAddress: {self.address}\nPhone number: {self.phone_number}\nDelivery time: {self.delivery_time}\n\n')
                for item in self.cart.items:
                    f.write(f'{item["product"].name}({item["attributes"]}): {item["product"].price}$(quantity:{item["quantity"]}) = {item["product"].price * item["quantity"]}$\n')
                f.write(f'Total price: {self.cart.get_total_price()}$')
        else: 
        # Payment failed
            with open('confirmation.txt', 'w') as f:
                f.write(f'Card number: {card_number}nStatus: Payment failednName: {self.name}')