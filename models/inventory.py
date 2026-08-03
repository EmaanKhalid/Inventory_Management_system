class Inventory:
    def __init__(self):
        self.__vehicles = {}
    @property
    def vehicles(self):
        return self.__vehicles

    def add_vehicle(self, vehicle):
        # Check if the vehicle ID already exists
        if vehicle.vehicle_id in self.__vehicles:
            print(f"Vehicle with ID '{vehicle.vehicle_id}' already exists.")
        else:
            self.__vehicles[vehicle.vehicle_id] = vehicle
            print(f"Vehicle '{vehicle.vehicle_id}' added successfully.")

    def remove_vehicle(self, vehicle_id):
        if vehicle_id in self.__vehicles:
            del self.__vehicles[vehicle_id]
            print(f"Vehicle '{vehicle_id}' removed successfully.")
        else:
            print(f"Vehicle '{vehicle_id}' not found.")

    def search_vehicle(self, vehicle_id):
        return self.__vehicles.get(vehicle_id)

    def display_inventory(self):
        if not self.__vehicles:
            print("Inventory is empty.")
        else:
            print("========== Vehicle Inventory ==========")
            for vehicle in self.__vehicles.values():
                vehicle.display_details()
                print("-" * 40)

    def update_vehicle_stock(self, vehicle_id, quantity):
        vehicle = self.search_vehicle(vehicle_id)

        if vehicle:
            vehicle.update_stock(quantity)
            print("Stock updated successfully.")
        else:
            print("Vehicle not found.")

    def display_available_vehicles(self):
        found = False

        for vehicle in self.__vehicles.values():
            if vehicle.is_available():
                vehicle.display_details()
                print("-" * 40)
                found = True

        if not found:
            print("No vehicles are available.")

    def calculate_inventory_value(self):
        total = 0

        for vehicle in self.__vehicles.values():
            total += vehicle.price * vehicle.stock_quantity

        return total

    def count_vehicles(self):
        return len(self.__vehicles)



