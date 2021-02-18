thermides = 3.9
kammenes_thermides = 0.0
x = 0
while x <= 30:
    kammenes_thermides = float(kammenes_thermides + thermides)
    x = x + 1
    if x == 10:
        print('Στα 10 λεπτά οι θερμίδες που έχετε κάψει είναι:',
              format(kammenes_thermides, ',.2f'), sep='')
    elif x == 15:
        print('Στα 15 λεπτά οι θερμίδες που έχετε κάψει είναι:',
              format(kammenes_thermides, ',.2f'), sep='')
    elif x == 20:
        print('Στα 20 λεπτά οι θερμίδες που έχετε κάψει είναι:',
              format(kammenes_thermides, ',.2f'), sep='')
    elif x == 25:
        print('Στα 25 λεπτά οι θερμίδες που έχετε κάψει είναι:',
              format(kammenes_thermides, ',.2f'), sep='')
    elif x == 30:
        print('Στα 30 λεπτά οι θερμίδες που έχετε κάψει είναι:',
              format(kammenes_thermides, ',.2f'), sep='')
