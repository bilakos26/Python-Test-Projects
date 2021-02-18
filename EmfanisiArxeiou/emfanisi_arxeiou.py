def ektelesi():
    emfanisi_arithmon()


def emfanisi_arithmon():
    file = open(r'C:\Users\bilakos\Desktop\PYTHON_TEST\EmfanisiArxeiou\numbers.txt', 'r')
    line = file.read()
    while line != '':
        print(line)
        line = file.read()
    file.close()


ektelesi()