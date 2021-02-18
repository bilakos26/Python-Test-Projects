imeres = int(input('Δώσε το πλήθος των ημερών: '))
misthos = 0.01
print()
print('Μισθός\t| Ημέρες', '\n----------------')
for x in range(1, imeres+1):
    misthos = float(misthos * 2)
    print('€', format(misthos, ',.2f'), '\t| ', x, sep='')
print()
print('Ο συνολικός μισθός είναι: €', format(misthos, ',.2f'), sep='')
