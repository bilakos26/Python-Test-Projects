# Μίλια = Χιλιόμετρα * 0,6214
def ektelesi():
    apostasi = xiliometra()
    milia = miles(apostasi)
    print('Τα ', format(apostasi, ',.2f'),
          ' χιλιόμετρα σε μίλια είναι: ', format(milia, ',.2f'), sep='')


def xiliometra():
    km = float(input('Δώσε τα μια απόσταση σε χιλιόμετρα: '))
    print()
    return km


def miles(apostasi):
    mp = float(apostasi * 0.6214)
    return mp


ektelesi()
