class Pet:

    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age


    def set_name(self, name):
        self.__name = name

    
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type


    def set_age(self, age):
        self.__age = age

    
    def get_name(self):
        return self.__name


    def get_animal_type(self):
        return self.__animal_type
    

    def get_age(self):
        return self.__age

    
    def __str__(self):
        return f"Pet name: {self.__name}\nAnimal Type: {self.__animal_type}\nPet Age: {self.__age}"


def main():
    print(entry())


def entry():
    name = input("Give the pet's name: ")
    print()
    animaltype = input("Give the pet's type: ")
    print()
    pet_age = input("Give the pet's age: ")
    print()
    pet = Pet(name, animaltype, pet_age)
    return pet

main()