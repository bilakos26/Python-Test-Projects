# Εθνικός φόρος 4% και Δημοτικός φόρος 2%
kostos_agoras = float(input('Δώσε μου το κόστος αγοράς: '))
ethnikos_foros = float(kostos_agoras * 0.04)
dimotikos_foros = float(kostos_agoras * 0.02)
synolikos_foros = float(ethnikos_foros + dimotikos_foros)
SynKosAgoras = float(kostos_agoras + synolikos_foros)
print('Το κόστος αγοράς είναι : €', format(kostos_agoras, ',.2f'), sep='')
print('Ο Εθνικός φόρος είναι: €', format(ethnikos_foros, ',.2f'), sep='')
print('Ο Δημοτικός φόρος είναι: €', format(dimotikos_foros, ',.2f'), sep='')
print('Το Συνολικό Κόστος αγοράς είναι: €', format(SynKosAgoras, ',.2f'),
      sep='')
