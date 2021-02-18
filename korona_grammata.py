# Το προγραμμα προσομειωνει την ριψη ενος κερματος, 10 φορες και θα εμφανιζει
# αν είναι κορώνα ή γράμμα.
import random


def ektelesi():
    x = 0
    while x != 10:
        tyxaios_arithmos()
        x = x + 1
        print()
    print()


def tyxaios_arithmos():
    arithmos = random.randint(1, 2)
    if arithmos == 1:
        print('Κορώνα')
    else:
        print('Γράμματα')


ektelesi()
