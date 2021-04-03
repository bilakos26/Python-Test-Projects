import pickle

def save_it(employees):
    with open(r'C:\Users\bilakos\Desktop\PYTHON_PROJECTS\PYTHON_TEST\System_Employees_Managment\employees.dat', 'wb') as emp_f:
        pickle.dump(employees, emp_f)


def load_it():
    try:
        with open(r'C:\Users\bilakos\Desktop\PYTHON_PROJECTS\PYTHON_TEST\System_Employees_Managment\employees.dat', 'rb') as emp_f:
            employees = pickle.load(emp_f)
    except Exception:
        emp_f = open(r'C:\Users\bilakos\Desktop\PYTHON_PROJECTS\PYTHON_TEST\System_Employees_Managment\employees.dat', 'wb')
        emp_f.close()
        emp_f = open(r'C:\Users\bilakos\Desktop\PYTHON_PROJECTS\PYTHON_TEST\System_Employees_Managment\employees.dat', 'rb')
        try:
            employees = pickle.load(emp_f)
            emp_f.close()
        except Exception:
            employees = {}
    return employees