def ektelesi():
    sum = 0
    for x in range(1, 5+1):
        inserted_grades = eisagogi_vathmon()
        sum = sum + inserted_grades
        determine_grade(inserted_grades)
    calc_average(sum)


def eisagogi_vathmon():
    vathmos = float(input('Δώσε τον βαθμό του διαγωνίσματος: '))
    print()
    return vathmos


def calc_average(sum):
    average = float(sum / 5)
    print('Το Σύνολο των βαθμών είναι: ', format(sum, ',.1f'), sep='')
    print()
    print('Ο Μέσος Όρος είναι: ', format(average, ',.1f'), sep='')
    print()
    return average


def determine_grade(inserted_grades):
    print('ΒΑΘΜΟΣ\t| ΒΑΘΜΟΣ-ΓΡΑΜΜΑ')
    print('-----------------------')
    if inserted_grades >= 90 and inserted_grades <= 100:
        print(format(inserted_grades, '.1f'), '\t| ', '    A')
        print()
    elif inserted_grades >= 80 and inserted_grades <= 89:
        print(format(inserted_grades, '.1f'), '\t| ', '    B')
        print()
    elif inserted_grades >= 70 and inserted_grades <= 79:
        print(format(inserted_grades, '.1f'), '\t| ', '    C')
        print()
    elif inserted_grades >= 60 and inserted_grades <= 69:
        print(format(inserted_grades, '.1f'), '\t| ', '    D')
        print()
    else:
        print(format(inserted_grades, '.1f'), '\t| ', '    F')
        print()


ektelesi()
