class Address:  # main class 
    def __init__(self, county_code:int, city_code:int, details:str, postal_code:str):  # force class attributes types
        self.country_code = county_code
        self.city_code = city_code
        self.details = details
        self.postal_code = postal_code
        self.afternoon_delivery_capacity = 3 # basic capacity for afternoon
        self.evening_delivery_capacity = 3   # basic capacity for evening

    def check_address(self):  # check correct address features
        # country code should be 1 for Tehran OR 2 for Esfahan OR 3 for Tabriz...
        # city code should be between the numbers 1 OR 2
        # postal code should have 10 digits
        if self.country_code in range(1,4) and self.city_code in range(1,3) and len(self.postal_code) == 10:
            return 'address is correct'
        else:
            return 'address is incorrect'
    
    def delivery_method(self):  #  assign delivery method
        if self.country_code == 1:  # if the city is Tehran
            return 'courier'
        else:
            return 'post'
            
    def choose_delivery_time(self):
        available_delivery_times = []  
        available_delivery_times.append('morning')  
        if self.afternoon_delivery_capacity > 0:  
            available_delivery_times.append('afternoon')
        if self.evening_delivery_capacity > 0:
            available_delivery_times.append('evening')  
        delivery_time = input(f'Enter delivery time {available_delivery_times}: ')
        if delivery_time == 'evening':
            self.evening_delivery_capacity -= 1  
        if delivery_time == 'afternoon':
            self.afternoon_delivery_capacity -= 1  
        return delivery_time