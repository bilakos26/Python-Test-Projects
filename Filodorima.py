# Το ποσό του φιλοδωρήματος είναι 15% και του φόρου 7%
katharo_kostos = float(input('Δώσε το καθαρό κόστος του γεύματός σου: €'))
filodorima = float(katharo_kostos * 0.15)
foros = float(katharo_kostos * 0.07)
synoliko_kostos = float(katharo_kostos + filodorima + foros)
print('Καθαρό Κόστος: €', format(katharo_kostos, ',.2f'), sep='')
print('Ποσό φιλοδωρήματος: €', format(filodorima, ',.2f'), sep='')
print('Ποσό φόρου: €', format(foros, ',.2f'), sep='')
print('Συνολικό Κόστος: €', format(synoliko_kostos, ',.2f'), sep='')
