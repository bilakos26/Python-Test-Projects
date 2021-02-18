def main():
    valid_numbers = dimiourgia_listas()
    elgxos_egkyrou_arithmou(valid_numbers)

def dimiourgia_listas():
    arxeio = open(r'C:\Users\bilakos\Desktop\ΠΡΟΓΡΑΜΜΑΤΑ & ΑΡΧΕΙΑ ΑΠΟ ΤΟ ΒΙΒΛΙΟ ΞΕΚΙΝΩΝΤΑΣ ΜΕ ΤΗΝ PYHTON\gaddis_python3_sourcecode\gaddis_python3_sourcecode\Chapter 07\charge_accounts.txt', 'r')
    lista = []
    for i in arxeio:
        i = i.rstrip('\n')
        i = int(i)  # Εάν δεν χρησιμοποιήσουμε το int(), τότε χρειαζόμαστε την παρακάτω συνάρτηση με το str()
        lista.append(i)
    arxeio.close()
    print(lista)
    return lista

def elgxos_egkyrou_arithmou(valid_numbers):
    ar_pistotikou_log = int(input('Δώσε έναν αριθμό πιστωτικού λογαριασμού: '))
    #ar_pistotikou_log = str(ar_pistotikou_log)
    if ar_pistotikou_log in valid_numbers:   #Πολύ σημαντικο να το θυμάμαι καθώς έτσι γίνεται αναζήτηση στις λίστες 
        print('Ο αριθμός είναι έγκυρος.')
    else:
        print('Ο αριθμός δεν είναι έγκυρος.')

main()