import pandas as pd  # importing pandas library

class Product:  # main class for product information
    def __init__(self, code, name, stock):
        self.code = code
        self.name = name
        self.stock = stock
        
class Warehouse:  # a class for warehouse information
    def __init__(self):
        self.products = []  # The warehouse list

    def add_product(self, product):
        self.products.append(product)

    def update_stock(self, code, buyed_quantity):
        for product in self.products:
            if product.code == code:
                product.stock = product.stock - buyed_quantity
                break

    def check_availability(self, code, quantity):
        for product in self.products:
            if product.code == code:
                if product.stock >= quantity:
                    return True
                else:
                    return False