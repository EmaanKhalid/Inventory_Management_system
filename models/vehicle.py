from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self,vehicle_id: str,brand: str, model: str,year: int,color: str,price: float,fuel_type: str,
            transmission: str,mileage: float,stock_quantity: int):
        self.__vehicle_id = vehicle_id
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__color = color
        self.price = price
        self.fuel_type = fuel_type
        self.transmission = transmission
        self.mileage = mileage
        self.stock_quantity = stock_quantity

    @property
    def vehicle_id(self):
        return self.__vehicle_id

    @property
    def brand(self):
        return self.__brand

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    @property
    def color(self):
        return self.__color

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value

    @property
    def mileage(self):
        return self.__mileage

    @mileage.setter
    def mileage(self, value):
        if value < 0:
            raise ValueError("Mileage cannot be negative.")
        self.__mileage = value

    @property
    def stock_quantity(self):
        return self.__stock_quantity

    @stock_quantity.setter
    def stock_quantity(self, value):
        if value < 0:
            raise ValueError("Stock cannot be negative.")
        self.__stock_quantity = value

    @property
    def fuel_type(self):
        return self.__fuel_type

    @fuel_type.setter
    def fuel_type(self, value):
        self.__fuel_type = value

    @property
    def transmission(self):
        return self.__transmission

    @transmission.setter
    def transmission(self, value):
        self.__transmission = value

    @abstractmethod
    def display_details(self):
        #Display details
        pass

    @abstractmethod
    def calculate_discount(self):
        #Return discounted amount
        pass

    @abstractmethod
    def calculate_tax(self):
        #Return tax amount
        pass

    def is_available(self):
        return self.stock_quantity > 0

    def update_price(self, new_price: float):
        #Update vehicle price.
        self.price = new_price

    def update_stock(self, quantity: int):
        if self.stock_quantity + quantity < 0:
            raise ValueError("Insufficient stock.")
        self.stock_quantity += quantity

    def get_final_price(self):
        discount = self.calculate_discount()
        tax = self.calculate_tax()
        return self.price - discount + tax

    def __str__(self):
        return (
            f"Vehicle ID : {self.vehicle_id}\n"
            f"Brand      : {self.brand}\n"
            f"Model      : {self.model}\n"
            f"Year       : {self.year}\n"
            f"Color      : {self.color}\n"
            f"Price      : {self.price}\n"
            f"Fuel Type  : {self.fuel_type}\n"
            f"Transmission: {self.transmission}\n"
            f"Mileage    : {self.mileage}\n"
            f"Stock      : {self.stock_quantity}"
        )
