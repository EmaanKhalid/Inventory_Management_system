from models.car import Car
from models.bike import Bike
from models.inventory import Inventory

inventory = Inventory()

car1 = Car(
    vehicle_id="C001",
    brand="Toyota",
    model="Corolla",
    year=2024,
    color="White",
    price=4200000,
    fuel_type="Petrol",
    transmission="Automatic",
    mileage=18,
    stock_quantity=5,
    number_of_doors=4,
    airbags=6,
    boot_capacity=470,
    sunroof=True
)

bike1 = Bike(
    vehicle_id="B001",
    brand="Honda",
    model="CB150F",
    year=2023,
    color="Black",
    price=350000,
    fuel_type="Petrol",
    transmission="Manual",
    mileage=45,
    stock_quantity=8,
    engine_capacity=150,
    bike_type="Sports",
    helmet_included=True
)

inventory.add_vehicle(car1)
inventory.add_vehicle(bike1)
inventory.display_inventory()
vehicle = inventory.search_vehicle("C001")
print('Vehicle found successfully:','\n',vehicle)
inventory.remove_vehicle("B001")
print(inventory.calculate_inventory_value())