import pickle


class Contacts:
    def __init__(self, name, phone, email):
        self.__name = name
        self.__phone = phone
        self.__email = email

    
    def set_name(self, name):
        self.__name = name


    def set_phone(self, phone):
        self.__phone = phone

    
    def set_email(self, email):
        self.__email = email


    def get_name(self):
        return self.__name


    def get_phone(self):
        return self.__phone


    def get_email(self):
        return self.__email


    def __str__(self):
        return "Name: " + self.__name +\
               "\nPhone: " + self.__phone +\
               "\nEmail: " + self.__email


LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

filename = r'C:\Users\bilakos\Desktop\PYTHON_PROJECTS\PYTHON_TEST\contacts.dat'

def main():
    mycontacts = load_contacts()
    
    choice = 0
    
    while choice != QUIT:
        choice = get_menu_choice()

        if choice == LOOK_UP:
            look_up(mycontacts)
        elif choice == ADD:
            add(mycontacts)
        elif choice == CHANGE:
            change(mycontacts)
        elif choice == DELETE:
            delete(mycontacts)
    
    save_contacts(mycontacts)


def load_contacts():
    try:
        with open(r'C:\Users\bilakos\Desktop\PYTHON_PROJECTS\PYTHON_TEST\contacts.dat', 'rb') as input_file:
            contact_dct = pickle.load(input_file)
    except Exception:
        #Αν το αρχείο contacts.dat δεν υπάρχει, τότε δημιουργείται μια εξαίρεση όπου δημιοργεί ένα άδειο λεξικό
        contact_dct = {}
    return contact_dct


def get_menu_choice():
    print()
    print('Menu')
    print('--------------------------------')
    print('1. Search contact')
    print('2. Add contact')
    print('3. Change contact')
    print('4. Delete contact')
    print('5. End of the program')
    print()
    
    choice = input('Give your choice: ')
    print()
    if choice == str(LOOK_UP) or choice == str(ADD) or choice == str(CHANGE) or choice == str(DELETE) or choice == str(QUIT):
        while choice < str(LOOK_UP) or choice > str(QUIT):
            print('Wrong insert. Please try again.')
            print()
            choice = input('Give your choice: ')
            print(''*2)
    else:
        while choice != str(LOOK_UP) and choice != str(ADD) and choice != str(CHANGE) and choice != str(DELETE) and choice != str(QUIT):
            print('Wrong insert. Please try again.')
            print()
            choice = input('Give your choice: ')
            print(''*2)
        while choice < str(LOOK_UP) or choice > str(QUIT):
            print('Wrong insert. Please try again.')
            print()
            choice = input('Give your choice: ')
            print(''*2)
    choice = int(choice)
    return choice


def look_up(mycontacts):
    name = input("Give a name to search: ")
    print(mycontacts.get(name, 'Not found.'))
    print()


def add(mycontacts):
    name = input('Give a name: ')
    
    if name not in mycontacts:
        phone = input('Give a phone number: ')
        email = input('Give an email: ')
        print()
        entry = Contacts(name, phone, email)

        mycontacts[name] = entry
        print('The contact name have been archived.')
        print()
    else:
        print('The contact name already exists.')
        print()


def change(mycontacts):
    name = input('Give a name to search: ')
    
    if name in mycontacts:
        phone = input('Give your new phone number: ')
        email = input('Give your new email address: ')
        print()
        entry = Contacts(name, phone, email)
        mycontacts[name] = entry
        print('The contact name has been updated.')
        print()
    else:
        print("The contact name doesn't exist.")
        print()


def delete(mycontacts):
    name = input('Give the name you want to delete from your contacts: ')

    if name in mycontacts:
        del mycontacts[name]
        print('The contact name has been successfully deleted.')
        print()
    else:
        print("The contact name doesn't exist.")
        print()
        

def save_contacts(mycontacts):
    with open(r'C:\Users\bilakos\Desktop\PYTHON_PROJECTS\PYTHON_TEST\contacts.dat', 'wb') as output_file:
        pickle.dump(mycontacts, output_file)


main()