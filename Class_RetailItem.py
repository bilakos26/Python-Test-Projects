class RetailItem:
    def __init__(self, description, storage_quantity, price):
        self.__description = description
        self.__storage_quantity = storage_quantity
        self.__price = price

    
    def set_description(self, description):
        self.__description = description


    def set_storage_quantity(self, storage_quantity):
        self.__storage_quantity = storage_quantity


    def set_price(self, price):
        self.__price = price


    def get_description(self):
        return self.__description


    def get_storage_quantity(self):
        return self.__storage_quantity


    def get_price(self):
        return self.__price


    def __str__(self):
        return (
            """
            Description: %s
            Storage Quantity: %s
            Product Price: %s
            """%(
                self.__description, self.__storage_quantity,
                self.__price
            )
        )


def main():
    p1 = RetailItem('Jacket', 12, 59.95)
    p2 = RetailItem('Trousers', 40, 34.95)
    p3 = RetailItem('Shirt', 20, 24.95)
    list_products = [p1, p2, p3]
    show_products(list_products)


def show_products(list_products):
    for product in list_products:
        print(product)


main()