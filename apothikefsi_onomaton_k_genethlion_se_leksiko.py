BIRTH_SEARCH = 1
ADD_BIRTH = 2
BIRTH_CHANGE = 3
DELETE_BIRTH = 4
CLOSE_PROGRAM = 5


def main():
    birthdays = {} #ή birthdays.dict()
    choise(birthdays)

def choise(birthdays):
    print('Φίλοι και τα γενέθλιά τους.')
    print("----------------------------")
    print('Δώσε μια από τις παρακάτω εντολές:\n1. Αναζήτηση γενεθλίων\n2. Προσθήκη νέων γενεθλίων\n'
          '3. Αλλαγή γενεθλίων\n4. Διαγραφή γενεθλίων\n5. Έξοδος του προγράμματος')
    ch = int(input("Δώσε την επιλογή σου: "))
    print(''*2)
    while ch < BIRTH_SEARCH or ch > CLOSE_PROGRAM:
        print('Λάθος αριθμός επιλογής. Ξανά προσπάθησε.')
        print('')
        print('Δώσε μια από τις παρακάτω εντολές:\n1. Αναζήτηση γενεθλίων\n2. Προσθήκη νέων γενεθλίων\n'
              '3. Αλλαγή γενεθλίων\n4. Διαγραφή γενεθλίων\n5. Έξοδος του προγράμματος')
        ch = int(input("Δώσε την επιλογή σου: "))
        print(''*2)
    while ch != CLOSE_PROGRAM:
        if ch == BIRTH_SEARCH:
            birth_search(birthdays)
        elif ch == ADD_BIRTH:
            add_birth(birthdays)
        elif ch == BIRTH_CHANGE:
            birth_change(birthdays)
        elif ch == DELETE_BIRTH:
            delete_birth(birthdays)
        print('Δώσε μια από τις παρακάτω εντολές:\n1. Αναζήτηση γενεθλίων\n2. Προσθήκη νέων γενεθλίων\n'
              '3. Αλλαγή γενεθλίων\n4. Διαγραφή γενεθλίων\n5. Έξοδος του προγράμματος')
        ch = int(input("Δώσε την επιλογή σου: "))
        print(''*2)
        while ch < BIRTH_SEARCH or ch > CLOSE_PROGRAM:
            print('Λάθος αριθμός επιλογής. Ξανά προσπάθησε.')
            print('')
            print('Δώσε μια από τις παρακάτω εντολές:\n1. Αναζήτηση γενεθλίων\n2. Προσθήκη νέων γενεθλίων\n'
                '3. Αλλαγή γενεθλίων\n4. Διαγραφή γενεθλίων\n5. Έξοδος του προγράμματος')
            ch = int(input("Δώσε την επιλογή σου: "))
            print(''*2)


def birth_search(birthdays):
    name = input('Δώσε όνομα για αναζήτηση: ')
    print(birthdays.get(name, 'Δε βρέθηκε.'))
    print(""*2)


def add_birth(birthdays):
    name = input("Δώσε όνομα για εισαγωγή: ")
    bday = input("Δώσε ημερομηνία γενεθλίων: ")
    if name not in birthdays:
        birthdays[name] = bday
    else:
        print("Η καταχώρηση υπάρχει ήδη.")
    print(""*2)


def birth_change(birthdays):
    name = input('Δώσε όνομα: ')
    if name in birthdays:
        bday = input("Δώσε νέα ημερομηνία γενεθλίων: ")
        birthdays[name] = bday
    else:
        print("Το όνομα δεν βρέθηκε.")
    print(""*2)


def delete_birth(birthdays):
    name = input("Δώσε όνομα: ")
    if name in birthdays:
        del birthdays[name]
    else:
        print('Το όνομα δεν βρέθηκε.')
    print(""*2)


main()