class Address:  # main class 
    def __init__(self, county_code:int, city_code:int, details:str, postal_code:str):  # force class attributes types
        self.country_code = county_code
        self.city_code = city_code
        self.details = details
        self.postal_code = postal_code

    def check_address(self):  # check correct address features
        # country code should be 1 for Tehran OR 2 for Esfahan OR 3 for Tabriz...
        # city code should be between the numbers 1 OR 2
        # postal code should have 10 digits
        if self.country_code in range(1,4) and self.city_code in range(1,3) and len(self.postal_code) == 10:
            return 'address is correct'
        else:
            return 'address is incorrect'