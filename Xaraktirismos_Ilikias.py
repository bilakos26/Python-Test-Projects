ilikia = float(input('Δώσε την ηλικία ενός ατόμου: '))
if ilikia <= 1:
    print('Το άτομο είναι βρέφος')
elif ilikia > 1 and ilikia < 13:
    print('Το άτομο είναι παιδί')
elif ilikia >= 13 and ilikia < 20:
    print('Το άτομο είναι έφηβος')
else:
    print('Το άτομο είναι ενήλικας')
