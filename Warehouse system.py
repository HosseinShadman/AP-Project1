import pandas as pd  # importing pandas library

class Product:  # main class for product information
    def __init__(self, code, name, stock):
        self.code = code
        self.name = name
        self.stock = stock