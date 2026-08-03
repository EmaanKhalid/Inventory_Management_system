class Customer:
    def __init__(self, customer_id:str, name:str, phone:str, address:str):
        self.__customer_id = customer_id
        self.__customer_name = name
        self.__customer_phone = phone
        self.__customer_address = address

    @property
    def customer_id(self):
        return self.__customer_id
    @property
    def customer_name(self):
        return self.__customer_name
    @property
    def customer_phone(self):
        return self.__customer_phone
    @property
    def customer_address(self):
        return self.__customer_address

    def display_customer_info(self):
        print(f"Customer ID: {self.__customer_id}")
        print(f"Customer Name: {self.__customer_name}")
        print(f"Customer Phone: {self.__customer_phone}")
        print(f"Customer Address: {self.__customer_address}")

