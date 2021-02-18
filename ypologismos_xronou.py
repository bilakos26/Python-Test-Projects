defterolepta = int(input('Δώσε τον αριθμό των δευτερολέπτων: '))
if defterolepta < 60:
    print('Δευτερόλεπτα: ', float(defterolepta), sep='')
elif defterolepta >= 60 and defterolepta < 3600:
    lepta = (defterolepta // 60) % 60
    defterolepta = defterolepta % 60
    print('Λεπτά: ', float(lepta), '\nΔευτερόλεπτα: ',
          float(defterolepta), sep='')
elif defterolepta >= 3600 and defterolepta < 86400:
    ores = defterolepta // 3600
    lepta = (defterolepta // 60) % 60
    defterolepta = defterolepta % 60
    print('Ώρες: ', float(ores), '\nΛεπτά: ', float(lepta), '\nΔευτερόλεπτα: ',
          float(defterolepta), sep='')
else:
    # Το 90000 είναι το αποτέλεσμα του 86400 + 3600 και το κάνουμε έτσι ώστε
    # στην δεύτερη 'else' να εμφανίζει μόνο τις ημέρες, τα λεπτά και τα
    # δευτερόλεπτα και όχι τις ώρες.
    if defterolepta >= 90000:
        imeres = (defterolepta // 3600) % 60
        imeres = imeres // 24
        ores = defterolepta - 86400
        ores = ores // 3600
        lepta = (defterolepta // 60) % 60
        defterolepta = defterolepta % 60
        print('Ημέρες: ', float(imeres), '\nΏρες: ', float(ores), '\nΛεπτά: ',
              float(lepta), '\nΔευτερόλεπτα: ', float(defterolepta), sep='')
    else:
        imeres = (defterolepta // 3600) % 60
        imeres = imeres // 24
        lepta = (defterolepta // 60) % 60
        defterolepta = defterolepta % 60
        print('Ημέρες: ', float(imeres), '\nΛεπτά: ', float(lepta),
              '\nΔευτερόλεπτα: ', float(defterolepta), sep='')
