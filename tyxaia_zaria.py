# Προσομείωση ρίψεις ζαριών
import random


def ektelesi():
    erotisi = 'YES'
    while erotisi == 'YES':
        tyxaia_zaria()
        erotisi = input('Θες να ξαναρίξεις τα ζάρια; Δώσε YES αν θες να'
                        ' συνεχίσεις, αλλιώς δώσε NO = ')
        print()


def tyxaia_zaria():
    print('Η πρώτη ζαριά είναι: ', random.randint(1, 6), sep='')
    print('Η δεύτερη ζαριά είναι: ', random.randint(1, 6), sep='')


ektelesi()
