def ektelesi():
    print('Το πρόγραμμα υπολογίζει τα μηνιαία κόστη για τις δαπάνες '
          'λειτουργίας του αυτοκινήτου\nΕπίσης, το πρόγραμμα υπολογίζει '
          'και το συνολικό ετήσιο κόστος των δαπανών του αυτοκινήτου '
          '(με βάση τα δεδομένα που έχετε εισάγει).')
    print()

    # Μεταφορά τον συναρτήσεων, σε μεταβλητές
    loan_payment = pliromi_daneiou()
    insurance = asfaleia_autokinitou()
    gas = venzini()
    oil = ladia_autokinitou()
    tires = elastika_autokinitou()
    maintenance = syntirisi_autokinitou()

    # Υπολογισμός μηνιαίου κόστους
    montly_cost = float(loan_payment + insurance + gas + oil + tires +
                        maintenance)
    print('Το μηνιαίο κόστος είναι €', format(montly_cost, ',.2f'), sep='')
    print()

    # Υπολογισμός ετήσιου κόστους
    Annual_cost = float(montly_cost * 12)
    print('Το ετήσιο κόστος είναι €', format(Annual_cost, ',.2f'), sep='')
    print()


def pliromi_daneiou():
    daneio = float(input('Δώσε την πληρωμή του δανείου: €'))
    print()
    return daneio


def asfaleia_autokinitou():
    asfaleia = float(input('Δώσε την ασφάλεια του αυτοκινήτου: €'))
    print()
    return asfaleia


def venzini():
    kafsima = float(input('Δώσε τα έξοδα για τις βενζίνες: €'))
    print()
    return kafsima


def ladia_autokinitou():
    ladia = float(input('Δώσε τα έξοδα για τα λάδια του αυτοκινήτου: €'))
    print()
    return ladia


def elastika_autokinitou():
    elastika = float(input('Δώσε τα έξοδα για τα ελαστικά του αυτοκινήτου: €'))
    print()
    return elastika


def syntirisi_autokinitou():
    syntirisi = float(input('Δώσε τα έξοδα για την συντήρηση του '
                            'αυτοκινήτου: €'))
    print()
    return syntirisi


ektelesi()
