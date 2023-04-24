import pandas as pd # importing pandas library

from Order_registration_system import Order # useing Order_registration_system module

class Successful_orders:  # main class for successful orders
    def __init__(self):
        self.orders = []  # The orders list
        
    def add_orders(self, number_of_goods, net_order_price, shipping_cost):
        order_number = Order().order_number
        tax = net_order_price * 0.09
        self.orders.append([number_of_goods, order_number, net_order_price, shipping_cost, tax])