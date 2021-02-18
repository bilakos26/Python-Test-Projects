# Το τελικό αποτέσμα στο συγκεκριμένο πρόβλημα για να έχει λογική προϋποθέτει
# την πώληση όλου του αριθμού των αγορασμένων μετοχών


arithmos_metoxon = float(input('Δώσε τον αριθμό των μετοχών που αγόρασες: '))
timi_metoxis = float(input('Δώσε την τιμή της μετοχής ανά μονάδα που '
                           'αγόρασες: €'))
poulimenes_metoxes = float(input('Δώσε τον αριθμό των μετοχών που πούλησες: '))
timi_polisis = float(input('Δώσε την τιμή πώλησης των μετοχών: €'))
promitheia = float(input('Δώσε την προμήθεια που θα πρέπει να καταβάλεις '
                         'στον χρηματιστή: '))
poso_agoras = float(arithmos_metoxon * timi_metoxis)
promitheia_agoras = float(poso_agoras * promitheia)
poso_polisis = float(poulimenes_metoxes * timi_polisis)
promitheia_polisis = float(poso_polisis * promitheia)
print('Το ποσό των χρημάτων που πλήρωσες για τις μετοχές είναι: €',
      format(poso_agoras, ',.2f'), sep='')
print('Το ποσό της προμήθειας που πλήρωσες για την αγορά των μετοχών είναι: €',
      format(promitheia_agoras, ',.2f'), sep='')
print('Το ποσό πώλησης των μετοχών είναι: €', format(poso_polisis, ',.2f'),
      sep='')
print('Το ποσό της προμήθειας που πλήρωσες για την πώληση των μετοχών είναι: '
      '€', format(promitheia_polisis, ',.2f'), sep='')
posoE = float(poso_polisis - promitheia_polisis)
kostos = float(poso_agoras + promitheia_agoras + promitheia_polisis)
kerdos = float(poso_polisis - kostos)
print('Το ποσό που σου έμεινε είναι: €', format(posoE, ',.2f'), sep='')
if poso_polisis > kostos:
    print('Έβγαλες κέρδος: €', format(kerdos, ',.2f'), sep='')
else:
    print('Έχασες λεφτά: €', format(kerdos, ',.2f'), sep='')
print('Η πληρωμή του χρηματιστή και τις δυο φορές ήτανε:\n'
      '1η φορά: €', format(promitheia_agoras, ',.2f'),
      '\n2η φορά: €', format(promitheia_polisis, ',.2f'), sep='')
