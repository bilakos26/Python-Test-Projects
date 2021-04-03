class Information:

    def __init__(self, name, address, age, phone_number):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_number = phone_number


    def set_name(self, name):
        self.__name = name


    def set_address(self, address):
        self.__address = address


    def set_age(self, age):
        self.__age = age


    def set_phone_number(self, phone_number):
        self.__phone_numer = phone_number


    def get_name(self):
        return self.__name


    def get_address(self):
        return self.__address


    def get_age(self):
        return self.__age

    
    def get_phone_number(self):
        return self.__phone_number


    def __str__(self):
        return f"Name: {self.__name}\nAddress: {self.__address}\nAge: {self.__age}" +\
            f"Phone Number: {self.__phone_number}"


def main():
    info = []
    for i in range(3):
        name = input('Give name: ')
        address = input('Give address: ')
        age = input('Give age: ')
        phone_number = input('Give phone number: ')
        print()
        person = Information(name, address, age, phone_number)

        info.append(person)

    for i in info:
        print(f"Name: {i.get_name()}\nAddress: {i.get_address()}\nAge: {i.get_age()}" +\
            f"Phone Number: {i.get_phone_number()}")


main()