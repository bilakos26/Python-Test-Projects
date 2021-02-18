# Το πρόγραμμα εμφανίζει δύο τυχαίους αριθμούς, τους οποίους θα πρέπει ο χρήστης να προσθέσεις.

import random


def ektelesi():
    num1, num2= tyxaioi_arithmoi()
    result = apotelesma_praksis(num1, num2)
    apantisi(result)


def tyxaioi_arithmoi():
    for x in range(2):
        arithmoi = random.randint(1, 1000)
        if x == 1:
            num1 = arithmoi
        else:
            num2 = arithmoi
    print('Πρόσθεσε αυτούς τους δύο αριθμούς:')
    print(num1)
    print(num2, ' +')
    print('_______')
    print()
    return num1, num2


def apotelesma_praksis(num1, num2):
    apotelesma =  num1 + num2
    return apotelesma


def apantisi(result):
    number = 0
    while result != number:
        number = int(input('Δώσε την σωστή απάντηση: '))
        print()
        if result == number:
            print('ΣΩΣΤΗ ΑΠΑΝΤΗΣΗ.')
            print()
        else:
            print('ΛΑΘΟΣ ΑΠΑΝΤΗΣΗ.', 'Παρακαλώ ξανά προσπάθησε.')
            print()


ektelesi()
