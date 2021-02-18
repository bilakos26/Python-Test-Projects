# Το πρόγραμμα υπολογίζει το χρηματικό ποσό που θα έχουμε στον τραπεζικό μας λογαριασμό μετά από έναν συγκεκριμένο αριθμό μηνών.
# F = Μελλοντική τιμή του ποσού, P = τρέχουσα τιμή του ποσού, i = μηνιαίο επιτόκιο, t = αριθμός των μηνών


def ektelesi():
    P, i, t = times()
    ypologismos(P, i, t)



def times():
    trexon_poso = float(input('Δώσε το τρέχον ποσό του τραπεζικού σου λογαριασμού: €'))
    print()
    miniaio_epitokio = float(input('Δώσε το μηνιαίο επιτόκιο: €'))
    print()
    mines = int(input('Δώσε τον αριθμό των μηνών που θα αφήσεις τα χρήματα στον λογαριασμό: '))
    print()
    return trexon_poso, miniaio_epitokio, mines


def ypologismos(P, i, t):
    mel_timi = float(P * ((1 + i) ** t))
    print('Το μελλοντικό ποσό, σύμφωνα με τα δεδομένα που εισάγατε είναι: €', format(mel_timi, ',.2f'), sep='')
    print()
    return mel_timi


ektelesi()