# Εθνικός φόρος 4% και Δημοτικός φόρος 2%
ETHNIKOS_FOROS = 0.04
DIMOTIKOS_FOROS = 0.02


def ektelesi():
    buy_cost = kostos_agoras()
    ethnikos_foros = float(buy_cost * ETHNIKOS_FOROS)
    dimotikos_foros = float(buy_cost * DIMOTIKOS_FOROS)
    synolikos_foros = float(ethnikos_foros + dimotikos_foros)
    SynKosAgoras = float(buy_cost + synolikos_foros)
    print('Το κόστος αγοράς είναι : €', format(buy_cost, ',.2f'), sep='')
    print()
    print('Ο Εθνικός φόρος είναι: €', format(ethnikos_foros, ',.2f'), sep='')
    print()
    print('Ο Δημοτικός φόρος είναι: €',
          format(dimotikos_foros, ',.2f'), sep='')
    print()
    print('Το Συνολικό Κόστος αγοράς είναι: €', format(SynKosAgoras, ',.2f'),
          sep='')


def kostos_agoras():
    kostos = float(input('Δώσε μου το κόστος αγοράς: '))
    print()
    return kostos


ektelesi()
