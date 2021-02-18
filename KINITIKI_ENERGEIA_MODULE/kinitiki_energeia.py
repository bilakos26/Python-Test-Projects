import mass
import speed


def ektelesi():
    kinetic_energy()


def kinetic_energy():
    m = float(input('Δώσε την μάζα του αντικειμένου σε κιλά: '))
    print()
    t = float(input('Δώσε την ταχύτητα του αντικειμένου σε μέτρα ανά '
                    'δευτερόλεπτο: '))
    print()
    KE = mass.maza(m) * speed.taxytita(t)
    print('Η κινητική ενέργεια του αντικειμένου, με βάση τα δεδομένα που '
          'εισάγατε είναι: ', format(KE, ',.2f'), sep='')
    print()


ektelesi()
