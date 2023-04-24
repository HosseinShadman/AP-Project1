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
    
    def manager_update_stock_from_textfile(self, file_path):
        with open(file_path, 'r') as f:  # reading a txt file
            for line in f:
                code, new_stock = line.strip().split(',')
                self.update_stock(code, int(new_stock))
    
    def manager_update_stock_from_csvfile(self, file_path):
        d = pd.read_csv(file_path)  # reading a txt file with pandas library
        for i in d.index:
            self.update_stock(d['code'][i], d['new_stock'][i])
            
    def manager_update_stock_manually(self):
        code = input("Enter product code: ")
        new_stock = int(input("Enter new stock: "))
        self.update_stock(code, new_stock)

    def check_availability(self, code, quantity):
        for product in self.products:
            if product.code == code:
                if product.stock >= quantity:
                    return True
                else:
                    return False
                              
    def get_stock(self):
        stock_list = []
        for product in self.products:
            stock_list.append([product.code, product.stock, 1])  # warehouse_code=1
        return stock_list
    
    def get_stock_in_textfile(self):
        with open('getstock.txt', 'w') as f:  # craet and write in a txt file
            for i in self.get_stock():
                f.write(f'code: {i[0]} , stock: {i[1]} , warehouse_code: {i[2]}')
                f.write('\n')
    
    def get_stock_in_csvfile(self):
        # creating a dataframe using pandas library
        d = pd.DataFrame(self.get_stock() , columns = ['code', 'stock', 'warehouse_code'])  
        d.to_csv('getstock.csv', index = False) # converting dataframe to a csv file