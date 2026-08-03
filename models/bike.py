from .vehicle import Vehicle

class Bike(Vehicle):
    def __init__(self,vehicle_id,brand,model,year,color,price,fuel_type,transmission,
                 mileage:float,stock_quantity:int,engine_capacity:float,
                 bike_type:str,helmet_included:bool):
        super().__init__(vehicle_id,brand,model,year,color,price,
                         fuel_type,transmission,mileage,stock_quantity)
        self.__engine_capacity = engine_capacity
        self.__bike_type = bike_type
        self.__helmet_included = helmet_included

    def display_details(self):
        print(super().__str__())
        print(f"engine_capacity         : {self.__engine_capacity}")
        print(f"bike_type       : {self.__bike_type}")
        print(f"helmet_included  : {self.__helmet_included} ")

    def calculate_discount(self):
        if self.year < 2024:
            return self.price * 0.08
        return 0
    def calculate_tax(self):
        return self.price * 0.10

bike1 = Bike('V002','Honda','CD 70',2020, 'black',70000,'petrol','Manual',
             12,7,72,'Commuter',False)
bike1.display_details()