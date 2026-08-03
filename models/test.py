from vehicle import Vehicle

class TestVehicle(Vehicle):

    def display_details(self):
        print(self)

    def calculate_discount(self):
        return 10000

    def calculate_tax(self):
        return 5000

vehicle = TestVehicle(
    vehicle_id="V001",
    brand="Toyota",
    model="Corolla",
    year=2024,
    color="White",
    price=4500000,
    fuel_type="Petrol",
    transmission="Automatic",
    mileage=18,
    stock_quantity=5
)
'''print(vehicle.vehicle_id)
print(vehicle.brand)
print(vehicle.model)
print(vehicle.year)
print(vehicle.color)
print(vehicle.price)
print(vehicle.fuel_type)
print(vehicle.transmission)
print(vehicle.mileage)
print(vehicle.stock_quantity)'''
print(vehicle.get_final_price())
#vehicle.display_details()