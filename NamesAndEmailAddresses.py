import pickle

ne = open('name_email.dat', 'rb')
NE = pickle.load(ne)
ne.close()
for i in NE.items():
    print(i)
print(''*2)

def main():
    cont = 'Y'
    while cont == 'Y' or cont == 'y':
        mc = menu_choices()
        if mc == 1:
            name = input('Give the First and the Last name: ')
            print('\n')
            name_email_search(name)
        elif mc == 2:
            name, email = name_email()
            add_name_email(name, email)
        elif mc == 3:
            name, email = name_email()
            change_email(name, email)
        else:
            name = input('Give the First and the Last name: ')
            print('\n')
            delete_name_email(name)
        print('Do you want to contine the program?\n')
        cont = input('Give Y/y for YES. Everything else = NO : ')
        print('')


def name_email():
    name = input('Give your First and Last name: ')
    email = input('\nGive your email: ')
    print('\n')
    return name, email


def menu_choices():
    print('- If you want to search a username and an email address, give 1\n- If you want to add a new username and email address, give 2\n'
        '- If you want to change an email address give 3\n- If you want to delete a username and the email address, give 4\n')
    mc = int(input('Give your choice: '))
    print('')
    while mc < 1 and mc > 4:
        print('\nWrong input. Please try again.')
        mc = int(input('Give your choice: '))
        print('')
    return mc


def name_email_search(name):
    if name in NE:
        ne = NE.get(name, "The name can't be found. Try again.\n")
        print('\n', name, ' : ', ne, sep='')
    else:
        print("The name can't be found. Try again.\n")


def add_name_email(name, email):
    ne = NE
    ne[name] = email 
    ne_f = open('name_email.dat', 'wb')
    pickle.dump(ne, ne_f)
    ne_f.close()
    print('The new username and email address has been added to the file.\n')


def change_email(name, email):
    if name in NE:
        NE[name] = email
        ne_f = open('name_email.dat', 'wb')
        pickle.dump(NE, ne_f)
        ne_f.close()
        print('The email has been changed.\n')
    else:
        print("The name can't be found. Try again.\n")


def delete_name_email(name):
    if name in NE:
        del NE[name]
        ne_f = open('name_email.dat', 'wb')
        pickle.dump(NE, ne_f)
        ne_f.close()
        print('The username and email address has been deleted from the file.\n')
    else:
        print("The name can't be found. Try again.\n")


main()