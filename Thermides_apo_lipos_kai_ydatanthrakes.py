# Θερμιδες λίπους = γραμμάρια λίπους * 9
# Θερμ΄ίδες από υδατάνθρακες = γραμμάρια υδατανθράκων * 4


def ektelesi():
    print('Το πρόγραμμα σας ζητάει τον αριθμό των γραμμαρίων λίπους και '
          'υδατανθράκων που καταναλώνετε την ημέρα, και υπολογίζει τον '
          'αριθμό των θερμίδων, που προέρχονται από το λίπος και από τους '
          'υδατάνθρακες.')
    print()
    fat_calories = grammaria_lipous()
    carb_calories = grammaria_ydatanthrakon()
    thermides_lipous(fat_calories)
    thermides_ydatanthrakon(carb_calories)


def grammaria_lipous():
    lipos = float(input('Δώσε τον αριθμό των γραμμαρίων λίπους που '
                        'καταναλώνεις την ημέρα: '))
    print()
    return lipos


def grammaria_ydatanthrakon():
    ydatanthrakes = float(input('Δώσε τον αριθμό τον αριθμό των γραμμαρίων '
                                'από υδατάνθρακες που καταναλώνεις την '
                                'ημέρα: '))
    print()
    return ydatanthrakes


def thermides_lipous(fat_calories):
    fat = float(fat_calories * 9)
    print('Οι θερμίδες λίπους είναι: ', format(fat, ',.2f'), sep='')
    print()
    return fat


def thermides_ydatanthrakon(carb_calories):
    carbs = float(carb_calories * 4)
    print('Οι θερμίδες υδατανθράκων είναι: ', format(carbs, ',.2f'), sep='')
    print()
    return carbs


ektelesi()
