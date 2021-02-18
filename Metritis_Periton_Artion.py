import random


def ektelesi():
    y = 0
    for x in range(1, 101):
        y = y + 1
        random_numbers = genitria_arithmon()
        print('Παραχθέντες Τυχαίοι Αριθμοί: ', y)
        print('---------------------------------')
        print()
        print('Τυχαίος Αριθμός: ', random_numbers)
        print()
        random_numbers = random_numbers % 2
        if random_numbers == 0:
            print('Ο αριθμός είναι ΆΡΤΙΟΣ.')
            print()
        else:
            print('Ο αριθμός είναι ΠΕΡΙΤΤΟΣ.')
            print()


def genitria_arithmon():
    arithmos = random.randint(1, 1001)
    return arithmos


ektelesi()