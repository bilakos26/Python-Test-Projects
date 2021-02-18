def main():
    list_creation = diavasma_listas()
    find_team(list_creation)


def diavasma_listas():
    arxeio = open(r'C:\Users\bilakos\Desktop\ΠΡΟΓΡΑΜΜΑΤΑ & ΑΡΧΕΙΑ ΑΠΟ ΤΟ ΒΙΒΛΙΟ ΞΕΚΙΝΩΝΤΑΣ ΜΕ ΤΗΝ PYHTON\gaddis_python3_sourcecode\gaddis_python3_sourcecode\Chapter 07\WorldSeriesWinners.txt', 'r')
    lista = []
    for i in arxeio:
        i = i.rstrip('\n')
        lista.append(i)
    return lista


def find_team(list_creation):
    team = input('Δώσε το όνομα της ομάδας: ')
    count = 0
    for i in list_creation:
        if i == team:
            count += 1
    print('Η ομάδα ', team, ' πήρε το πρωτάθλημα από το 1903 έως το 2009, ', count, ' φορές.', sep='')


main()