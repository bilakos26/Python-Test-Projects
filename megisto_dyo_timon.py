# Δεχετε δύο τυχαιες ακέραιες τιμές και επιστρέφει την μεγαλύτερη

import random


def ektelesi():
    num1, num2 = eisodos_arithmon()
    maximum(num1, num2)


def eisodos_arithmon():
    for x in range(2):
        arithmos = random.randint(1, 100)  # εισάγει τους τυχαίους αριθμούς
        if x == 1:
            num1 = arithmos
        else:
            num2 = arithmos
    print('Οι δύο αριθμοί είναι: ', num1, 'και', num2)
    print()
    return num1, num2


def maximum(num1, num2):
    if num1 > num2:
        print('Η μεγαλύτερη τιμή, από τις δύο τιμές είναι το ', num1)
    else:
        print('Η μεγαλύτερη τιμή, από τις δύο τιμές είναι το ', num2)


ektelesi()
