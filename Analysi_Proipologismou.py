proipologismos = float(input('Δώσε ένα χρηματικό σκοπό που έχεις αποφασίσει '
                             'να δαπανήσεις σε έναν μήνα: €'))
print()
eksoda = float(input('Δώσε τα έξοδά σου για αυτόν τον μήνα '
                     'ή δώσε 0 για τερματισμό: €'))
dapani = 0.0
print()
while eksoda != 0:
    dapani = dapani + eksoda
    eksoda = float(input('Δώσε τα έξοδά σου για αυτόν τον μήνα '
                         'ή δώσε 0 για τερματισμό: €'))
    print()
if dapani < proipologismos:
    print('Η δαπάνες σας, είναι κάτω από τον προϋπολογισμό σας: \n',
          'Δαπάνες\t| Προϋπολογισμός', '\n------------------------\n',
          '€', format(dapani, ',.2f'), ' | €', format(proipologismos, ',.2f'),
          sep='')
    proipologismos = float(proipologismos - dapani)
    print('Έχετε περιθώριο: ', format(proipologismos, ',.2f'), '€ ακόμη',
          sep='')
elif dapani > proipologismos:
    print('Η δαπάνες σας, είναι πάνω από τον προϋπολογισμό σας: \n',
          'Δαπάνες\t| Προϋπολογισμός', '\n------------------------\n',
          '€', format(dapani, ',.2f'), ' | €', format(proipologismos, ',.2f'),
          sep='')
    proipologismos = float(proipologismos - dapani)
    # Σε αυτό το σημείο αφαιρούμε το αρνητικό πρόσημο.
    proipologismos = float(proipologismos * (-1))
    print('Έχετε υπερβεί το προϋπολογισμό κατα: €',
          format(proipologismos, ',.2f'), sep='')
else:
    print('Οι δαπάνες σας, είναι ισότιμες με τον προϋπολογισμό σας: \n',
          'Δαπάνες\t| Προϋπολογισμός', '\n------------------------\n',
          '€', format(dapani, ',.2f'), ' | €', format(proipologismos, ',.2f'),
          sep='')
