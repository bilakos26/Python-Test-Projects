# Η Αντικειμενική αξία υπολογίζεται ως εξής: Εμπορική αξία * 60% ή 0,6
# Ο φόρος περιουσιακών είναι 0,72 λεπτά για κάθε 100€, δηλαδή:
'(Αντ. Αξ. * 0,72) / 100'

ANTIKEIMENIKI_AKSIA = 0.6
FOROS = 0.72


def ektelesi():
    print('Ο σκοπός αυτού του προγράμματος είναι ο υπολογισμός της '
          'αντικειμενικής αξίας και του φόρου του οικοπέδου, με την εισαγωγή '
          'της εμπορικής αξίας του οικοπέδου.')
    print()
    market_value = emporiki_aksia()
    objective_value = antikimeniki_aksia(market_value)
    land_tax = foros_oikopedou(objective_value)
    print('Η αντικειμενική αξία του οικοπέδου είναι €',
          format(objective_value, ',.2f'), '\n',
          '\nΟ φόρος του οικοπέδου '
          'είναι €', format(land_tax, ',.2f'), sep='')


'############################### ΣΥΝΑΡΤΗΣΕΙΣ ################################'


def emporiki_aksia():
    aksia = float(input('Δώσε την εμπορική αξία ενός οικοπέδου: €'))
    print()
    return aksia


def antikimeniki_aksia(market_value):
    timi = float(market_value * ANTIKEIMENIKI_AKSIA)
    return timi
# Εάν δεν είχα βάλει την μεταβλητή timi και την εντολή return
# Θα μου επέστρεφε σφάλμα!!
# Έτσι θα με ανάγκαζε να κάνω τις πράξεις μέσα στην συνάρτηση της ΕΚΤΕΛΕΣΗΣ
# του προγράμματος.


def foros_oikopedou(objective_value):
    foros = float((objective_value * 0.72) / 100)
    return foros


ektelesi()
