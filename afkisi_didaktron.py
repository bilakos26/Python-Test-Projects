didaktra = 16000.0
afkisi = 0.03
mines = 0
print('Ποσά διδάκτρων για τα επόμενα 5 έτη, με αύξηση 3% το χρόνο:')
for x in range(1, 6):
    poso_afksisis = didaktra * afkisi
    didaktra = float(didaktra + poso_afksisis)
    posa = float(didaktra / 2)
    print('Ποσά', '\t|', 'Μήνες', '\t|', 'Έτος', '\n----------------------',
          sep='')
    print('Δίδακτρα = €', format(didaktra, ',.2f'), sep='')
    for y in range(2):
        mines = mines + 1
        print(format(posa, ',.2f'), "|\t", int(mines), '|\t', int(x), sep='')
        print()
