import random


def ektelesi():
    try:
        EntryRandomNumbers = PlithosTyxaionArithmon()
        GenitriaTyxaionArithmon(EntryRandomNumbers)
        EmfanisiArithmon()
    except IOError:
        print('Πρόβλημα με το άνοιγμα του αρχείου')
    except ValueError:
        print('Βρέθηκαν μη αριθμητικά στοιχεία')


def PlithosTyxaionArithmon():
    arithmos = int(input('Πόσους τυχαίους αριθμούς θέλετε να εισάγετε στο αρχείο; '))
    print()
    return arithmos


def GenitriaTyxaionArithmon(EntryRandomNumbers):
    file_name = open(r'C:\Users\bilakos\Desktop\PYTHON_TEST\EmfanisiArxeiou\random_numbers.txt', 'a')
    for i in range(1, EntryRandomNumbers + 1):
        tyxaios_ar = random.randint(1, 501)
        file_name.write(str(tyxaios_ar) + '\n')
    file_name.close()


def EmfanisiArithmon():
    file_name = open(r'C:\Users\bilakos\Desktop\PYTHON_TEST\EmfanisiArxeiou\random_numbers.txt', 'r')
    y = 0
    total = 0
    for line in file_name:
        y += 1
        num = int(line)
        total += num
        print('#', y, ': ', num, sep='')
    print('Το άθροισμα των αριθμών είναι: ', total)
    file_name.close()


ektelesi()