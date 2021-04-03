import employee_class


def search_Employee(employees):
    ID = input("Give the employee ID: ")
    print()
    if ID in employees:
        print(employees[ID])
    else:
        print("The ID number couldn'y be found.")
        print()



def choice():
    choise = int(input('1) Give 1 to search an employee\n2) Give 2 to Add a new employee\n3) Give 3 to modify the name, the department, '
                   'and the job title of an employee.\n3) Give 4 to Delete an employee\n5) Give 5 to Exit the program\nGive your choise: '))
    print()
    while choise < 1 or choise > 5:
        print('Wrong input. Try again.')
        print()
        choise = int(input('1) Give 1 to search an employee\n2) Give 2 to Add a new employee\n3) Give 3 to modify the name, the department, '
                   'and the job title of an employee.\n3) Give 4 to Delete an employee\n5) Give 5 to Exit the program\nGive your choise: '))
    return choise


def add_employee(employees):
    name = input('Give the name of the employee: ')
    ID = input('Give employee ID: ')
    department = input('Give the department of the employee: ')
    job_title = input('Give the Job Title of the employee: ')
    print()
    if ID not in employees:
        employees[ID] = employee_class.Employee(name, ID, department, job_title)
        print('SAVED!')
        print()
    else:
        print('An entry with that ID already exists.')
        print()


def change(employees):
    ID = input('Give the ID number of the empoloyee you want to change: ')

    if ID in employees:
        name = input('Give the name of the employee: ')
        department = input('Give the department of the employee: ')
        job_title = input('Give the Job Title of the employee: ')
        employees[ID] = employee_class.Employee(name, ID, department, job_title)
        print('DATA CHANGED!')
        print()
    else:
        print('That ID number already exists.')


def delete(employees):
    ID = input('Give the ID number of the employee that you want to delete: ')
    if ID in employees:
        del employees[ID]
        print('EMPLOYEE DELETED!')
        print()
    else:
        print('That ID number already exists.')