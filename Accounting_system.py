import pandas as pd # importing pandas library

from Order_registration_system import Order # useing Order_registration_system module

class Successful_orders:  # main class for successful orders
    def __init__(self):
        self.orders = []  # The orders list
        
    def add_orders(self, number_of_goods, net_order_price, shipping_cost):
        order_number = Order().order_number
        tax = net_order_price * 0.09
        self.orders.append([number_of_goods, order_number, net_order_price, shipping_cost, tax])
        
    def csv_output(self):
        d = pd.DataFrame(self.orders , columns = ['number_of_goods', 'order_number', 'net_order_price', 'shipping_cost', 'tax'])
        # creating a dataframe using pandas library
        d.to_csv('output.csv', index = False)  # converting dataframe to a csv file     

    def text_output(self):
        with open('output.txt', 'w') as f:  # craet and write in a txt file
            for i in self.orders:
                f.write(f'number_of_goods: {i[0]} , order_number: {i[1]} , net_order_price: {i[2]} , shipping_cost: {i[3]} , tax: {i[4]}')
                f.write('\n')