lianiki_timi = 99
posotita = int(input('Δώσε τον αριθμό των εφαρμογών που αγόρασες: '))
kostos = lianiki_timi * posotita
if posotita < 10:
    print('Έκπτωση: €0', '\nΣυνολικό Κόστος: €',
          format(kostos, ',.2f'), sep='')
elif posotita >= 10 and posotita <= 19:
    ekptosi = float(kostos * 0.2)
    synoliko_kostos = kostos - ekptosi
    print('Κόστος: €', format(kostos, ',.2f'), '\nΈκπτωση: €',
          format(ekptosi, ',.2f'), '\nΣυνολικό Κόστος: €',
          format(synoliko_kostos, ',.2f'), sep='')
elif posotita >= 20 and posotita <= 49:
    ekptosi = float(kostos * 0.3)
    synoliko_kostos = kostos - ekptosi
    print('Κόστος: €', format(kostos, ',.2f'), '\nΈκπτωση: €',
          format(ekptosi, ',.2f'), '\nΣυνολικό Κόστος: €',
          format(synoliko_kostos, ',.2f'), sep='')
elif posotita >= 50 and posotita <= 99:
    ekptosi = float(kostos * 0.4)
    synoliko_kostos = kostos - ekptosi
    print('Κόστος: €', format(kostos, ',.2f'), '\nΈκπτωση: €',
          format(ekptosi, ',.2f'), '\nΣυνολικό Κόστος: €',
          format(synoliko_kostos, ',.2f'), sep='')
else:
    ekptosi = float(kostos * 0.5)
    synoliko_kostos = kostos - ekptosi
    print('Κόστος: €', format(kostos, ',.2f'), '\nΈκπτωση: €',
          format(ekptosi, ',.2f'), '\nΣυνολικό Κόστος: €',
          format(synoliko_kostos, ',.2f'), sep='')
