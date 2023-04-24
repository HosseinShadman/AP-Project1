class Address:  # main class 
    def __init__(self, county_code:int, city_code:int, details:str, postal_code:str):  # force class attributes types
        self.country_code = county_code
        self.city_code = city_code
        self.details = details
        self.postal_code = postal_code
