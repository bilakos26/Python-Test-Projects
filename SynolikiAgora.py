# Το φόρος είναι 6%
proion1 = float(input("Δώσε την τιμή του 1ου προϊόντος: "))
proion2 = float(input("Δώσε την τιμή του 2ου προϊόντος: "))
proion3 = float(input("Δώσε την τιμή του 3ου προϊόντος: "))
proion4 = float(input("Δώσε την τιμή του 4ου προϊόντος: "))
proion5 = float(input("Δώσε την τιμή του 5ου προϊόντος: "))
meriko_synolo = float(proion1 + proion2 + proion3 + proion4 + proion5)
foros = float(meriko_synolo * 0.06)
teliko_synolo = float(meriko_synolo + foros)
print("Μερικό Σύνολο: €", format(meriko_synolo, ',.2f'), sep='')
print("Φόρος: €", format(foros, ',.2f'), sep='')
print("Τελικό Σύνολο: €", format(teliko_synolo, ',.2f'), sep='')
