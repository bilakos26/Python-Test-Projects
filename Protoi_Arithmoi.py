def ektelesi():
    x = 0
    for x in range(100):
        x = x + 1
        print('Ο αριθμός είναι: ', x)
        number = is_prime(x)
        if number == True:
            print('Ο αριθμός είναι πρώτος αριθμός')
            print()
        else:
            print('Ο αριθμός δεν είναι πρώτος αριθμός')
            print()


def is_prime(x):
    protos = x % 2
    if x == 0:
        status = False
    elif x == 1:
        status = False
    elif x == 2:
        status = True
    elif protos != 0:  # Εδώ ορίζουμε όλους τους πρώτους αριθμούς
        status = True
    else:
        status = False
    return status


ektelesi()