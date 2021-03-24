import random
from time import sleep

class Coin:

    #Αν αλλάξουμε το sideup σε __sideup, τοτε απο public μέθοδος μετατρέπεται σε private
    def __init__(self):
        self.__sideup = 'Κορώνα'


    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Κορώνα'
        else:
            self.__sideup = 'Γράμματα'
    

    def get_sideup(self):
        return self.__sideup


def main():
    my_coin = Coin()

    print('Η επάνω πλευρά είναι: ', my_coin.get_sideup())

    print('Ρίχνω το κέρμα ...')
    my_coin.toss()
    #Παρόλο που την καλούμε, δεν ορίζεται σε Κορώνα γιατι μεσα στην κλάση την εχουμε private. Σε αντίθετη περίπτωση 
    #αν βάζαμε my_coin.sideup = 'Κορώνα', τότε σε κάθε επανάληψη θα είχαμε το ίδιο αποτέλεσμα.
    my_coin.__sideup = 'Κορώνα'
    sleep(2)
    print('Η επάνω πλευρά είναι: ', my_coin.get_sideup())


main()