# 1 πόδι = 12 ίντσες


def ektelesi():
    foot_number = arithmos_podion()
    calculation = ypologismos(foot_number)
    ektyposi(calculation)


def arithmos_podion():
    podia = int(input('Δώσε τον αριθμό ποδιών που θέλεις να υπολογίσεις σε ίντσες: '))
    print()
    return podia

def ypologismos(foot_number):
    synolo = float(foot_number * 12)
    return synolo


def ektyposi(calculation):
    print('Ο αριθμός των ποδιών σε ίντσες είναι: ', format(calculation, ',.2f'), sep='')


ektelesi()