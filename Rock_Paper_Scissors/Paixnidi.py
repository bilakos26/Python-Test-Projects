import random
import rock
import scissors
import paper


def ektelesi():
    erotisi = 'Y'
    while erotisi != 'N':
        print('Παιχνίδι Πέτρα, Ψαλίδι, Χαρτί.')
        print('------------------------------')
        pc_choice = ypologistis()
        user = xristis(Menu_epilogon)
        print('-Επιλογή υπολογιστή ', epilogi_ypologisti(pc_choice) )
        epilogi_xristi(user)
        if user == 1:  # Με την απάντηση του χρήστη, δίνουμε την δυνατότητα στο πρόγραμμα να προσδιορίσει με αυτόν τον τρόπο τον ΝΙΚΗΤΗ
            rock.petra(user, pc_choice)  # 1  Παίρνει τις εντολές από το import rock
        elif user == 2:
            scissors.psalidi(user, pc_choice)  # 2  Παίρνει τις εντολές από το import scissors
        else:
            paper.xarti(user, pc_choice)  # 3  Παίρνει τις εντολές από το import paper
        erotisi = input('Θέλετε να ξανά παίξετε; Σε λατινικούς χαρακτήρες, αν θέλετε να συνεχίσετε δώστε Y, αλλιώς αν όχι δώστε Ν. =  ')


def ypologistis():
    tyxaios_arithmos = random.randint(1, 3)
    return tyxaios_arithmos


def xristis(Menu_epilogon):
    Menu_epilogon()
    epilogi = int(input('Επέλεξε Πέτρα, Ψαλίδι ή Χαρτί, απέναντι στον υπολογιστή: '))
    print()
    while epilogi != 1 and epilogi != 2 and epilogi != 3:
        print('Έχεις δώσει λανθασμένη απάντηση. Παρακαλώ ξανά προσπάθησε')
        print()
        Menu_epilogon()
        epilogi = int(input('Επέλεξε Πέτρα, Ψαλίδι ή Χαρτί, απέναντι στον υπολογιστή: '))
        print()
    return epilogi


def Menu_epilogon():
    print('Αν θες Πέτρα δώσε το 1\nΑν θες Ψαλίδι δώσε το 2\nΑν θες Χαρτί δώσε το 3')


def epilogi_ypologisti(pc_choice):
    epilogi = ''
    if pc_choice == 1:
        epilogi = 'Πέτρα'
    elif pc_choice == 2:
        epilogi = 'Ψαλίδι'
    else:
        epilogi = 'Χαρτί'
    
    return epilogi


def epilogi_xristi(user):
    if user == 1:
        print('-Επιλέξατε Πέτρα')
        print()
    elif user == 2:
        print('-Επιλέξατε Ψαλίδι')
        print()
    else:
        print('-Επιλέξατε Χαρτί')
        print()


ektelesi()