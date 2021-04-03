#ΑΣΚΗΣΗ 6 CLASSES
import save_data
import menu_choices

SEARCH = 1
ADD = 2
CHANGE = 3
DELETE = 4
EXIT = 5

def main():
    #ΑΣΚΗΣΗ 4
    #obj1 = Employee('Susan Meyers', 47899, 'Accounting', 'Vice Precident')
    #obj2 = Employee('Mark Jones', 39119, 'IT', 'Programmer')
    #obj3 = Employee('Joy Rogers', 81774, 'Manifacturing', 'Engineer')
    #list_obj = [obj1, obj2, obj3]
    #show_obj(list_obj)
    employees = save_data.load_it()
    choice = menu_choices.choice()
    while choice != EXIT:
        if choice == SEARCH:
            menu_choices.search_Employee(employees)
        elif choice == ADD:
            menu_choices.add_employee(employees)
        elif choice == CHANGE:
            menu_choices.change(employees)
        elif choice == DELETE:
            menu_choices.delete(employees)

        choice = menu_choices.choice()

    save_data.save_it(employees)
    print("DATA SAVED!")
    print()

#def show_obj(list_obj):
#    for obj in list_obj:
#        print(obj)


main()