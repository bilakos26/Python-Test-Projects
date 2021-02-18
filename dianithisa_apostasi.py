# Απόσταση = Ταχύτητα * Χρόνος
taxitita = float(input('Δώσε την ταχύτητα του οχήματος (σε km/h): '))
print()
ora = int(input('Δώσε τον αριθμό των ωρών που έχει ταξιδέψει: '))
print()
print('Ώρα\t|   Διανυθείσα Απόσταση')
print('-----------------------------')
for x in range(1, ora+1):
    apostasi = float(taxitita * x)
    print(int(x), '\t|   ', format(apostasi, ',.2f'), sep='')
