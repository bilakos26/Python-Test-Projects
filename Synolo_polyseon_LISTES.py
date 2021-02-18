def main():
    entry_sales = eisagogi_polyseon()
    synolo_polyseon(entry_sales)

def eisagogi_polyseon():
    polyseis = []
    print('Δώσε τα ποσά των πωλήσεων για κάθε μέρα της εβδομάδας')
    erotisi = 'Y'
    while erotisi == 'Y' or erotisi == 'y' or erotisi == 'Ν' or erotisi == 'ν':
        m = 0
        for i in range(1, 8):
            m += 1
            print('Δώσε το ποσό της ', m, 'ης ημέρας της εβδομάδας: ', sep='')
            poso = float(input())
            polyseis.append(poso)
        print('Θέλεις να προσθέσεις κι άλλα εβδομαδιαία ποσά στην λίστα;')
        erotisi = input('Δώσε Y/y ή Ν/ν για ΝΑΙ. Οτιδήποτε άλλο = ΟΧΙ. : ')
    print(polyseis)
    return polyseis


def synolo_polyseon(entry_sales):
    synolo = 0
    for i in entry_sales:
        synolo += i
    print('Το σύνολο των πωλήσεων είναι: ', format(synolo, ',.2f'), '€', sep='')
    return synolo

main()