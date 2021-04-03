class Car:

    def __init__(self, y_model, brand, speed):
        self.__year_model = y_model
        self.__make = brand
        self.__speed = 0


    def set_year_model(self, y_model):
        self.__year_model = y_model


    def set_make(self, make):
        self.__make = make

    
    def set_speed(self, speed):
        self.__speed = 0


    def get_year_model(self):
        return self.__year_model


    def get_make(self):
        return self.__make


    #Methods
    def accelerate(self):
        self.__speed += 5


    def brake(self):
        self.__speed -= 5

    
    def get_speed(self):
        return self.__speed


def main():
    year = input('Enter the car year: ')
    make = input('Enter the car make: ')
    speed = 0

    my_car = Car(year, make, speed)
    first(my_car)
    second(my_car)


def first(my_car):
    for i in range(5):
        my_car.accelerate()
        print(f'The current speed is: {my_car.get_speed()}')
        print()


def second(my_car):
    for i in range(5):
        my_car.brake()
        print(f'The current speed after brake is: {my_car.get_speed()}')
        print()

    
main()