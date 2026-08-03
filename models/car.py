from .vehicle import Vehicle

class Car(Vehicle):
    def __init__(self,
        vehicle_id: str,
        brand: str,
        model: str,
        year: int,
        color: str,
        price: float,
        fuel_type: str,
        transmission: str,
        mileage: float,
        stock_quantity: int,
        number_of_doors: int,
        airbags: int,
        boot_capacity: float,
        sunroof: bool):
        super().__init__(vehicle_id,
            brand,
            model,
            year,
            color,
            price,
            fuel_type,
            transmission,
            mileage,
            stock_quantity)
        self.__number_of_doors = number_of_doors
        self.__airbags = airbags
        self.__boot_capacity = boot_capacity
        self.__sunroof = sunroof

    def display_details(self):
        print(super().__str__())
        print(f"Doors          : {self.__number_of_doors}")
        print(f"Airbags        : {self.__airbags}")
        print(f"Boot Capacity  : {self.__boot_capacity} L")
        print(f"Sunroof        : {self.__sunroof}")

    def calculate_discount(self):
        if self.year < 2022:
            return self.price * 0.10
        return 0

    def calculate_tax(self):
        return self.price * 0.12

    def start_engine(self):
        print(f"{self.brand} {self.model} engine started.")

'''vehicle_id = input("Enter Vehicle ID: ")
brand = input("Enter Brand: ")
model = input("Enter Model: ")
year = int(input("Enter Year: "))
color = input("Enter Color: ")
price = float(input("Enter Price: "))
fuel_type = input("Enter Fuel Type: ")
transmission = input("Enter Transmission: ")
mileage = float(input("Enter Mileage: "))
stock_quantity = int(input("Enter Stock Quantity: "))

number_of_doors = int(input("Enter Number of Doors: "))
airbags = int(input("Enter Number of Airbags: "))
boot_capacity = float(input("Enter Boot Capacity: "))

sunroof = input("Sunroof (True/False): ").lower() == "true"

car1 = Car(vehicle_id,brand,model,year,color,price,fuel_type,transmission,mileage,stock_quantity,number_of_doors,airbags,
    boot_capacity,sunroof)
car2 = Car(vehicle_id,brand,model,year,color,price,fuel_type,transmission,mileage,stock_quantity,number_of_doors,airbags,
    boot_capacity,sunroof)



car1.display_details()'''

