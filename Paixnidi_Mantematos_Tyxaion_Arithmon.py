import random


def ektelesi():
    question = 'Y'
    while question != 'N':
        random_number = tyxaios_arithmos()
        mantepse(random_number)
        question = input('Θέλεις να συνεχίσεις το παιχνίδι; Αν θέλεις τότε με λατινικούς χαρακτήρες '
                         'δώσε Y. Αν δεν επιθυμείς να συνεχίσεις τοτε δώσε N. =  ')


def tyxaios_arithmos():
    arithmos = random.randint(1, 101)
    print(arithmos)
    return arithmos


def mantepse(random_number):
    x = 0
    apantisi_xristi = int(input('Μάντεψε ποιός είναι ο αριθμός: '))
    while apantisi_xristi != random_number:
        if apantisi_xristi > random_number:
            x = x + 1
            print('Πολύ ψηλή τιμή, παρακαλώ ξανά προσπάθησε.')
            print()
            apantisi_xristi = int(input('Μάντεψε ποιός είναι ο αριθμός: '))
            print()
        elif apantisi_xristi < random_number:
            x = x + 1
            print('Πολύ χαμηλή τιμή, παρακαλώ ξανά προσπάθησε.')
            print()
            apantisi_xristi = int(input('Μάντεψε ποιός είναι ο αριθμός: '))
            print()
    else:
        print('Σωστή απάντηση!!!')
        print('Προσπάθειες μέχρι να βρείς την απάντηση: ', x)


ektelesi()