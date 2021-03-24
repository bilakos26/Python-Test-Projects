import random

def main():
    print("Παιχνίδι Ερωτήσεων με Πρωτεύουσες Νομών.")
    print('----------------------------------------')
    print('')
    cc = CountryCapitals()
    len_cp = len(CountryCapitals())
    counter = 0
    t_a = 0
    f_a = 0
    question = 0
    while counter != len_cp:
        question += 1
        pr = random.choice(list(cc.keys())) #Η μέθοδος popitem() έπερνε πάντα το τελευταίο στοιχείο της λίστας πράγμα που την καθιστά προκαθορισμένη.
        print(f'{question}) ', pr)
        answer = input('Ποιά είναι η Πρωτεύουσα του Νομού; ')
        print('')
        if answer == cc[pr]:
            print(f"Σωστή απάντηση.\n{pr} = {cc[pr]}.")
            t_a += 1
            del cc[pr]
        else:
            print(f'Λάθος απάντηση.\nΗ απάντηση ήτανε: {pr} = {cc[pr]}.')
            f_a += 1
            del cc[pr]
        print("" * 2)
        counter += 1
    print(f'Τέλος Παιχνιδιού.\nΣωστές απαντήσεις: {t_a}\nΛάθος απαντήσεις: {f_a}')


def CountryCapitals():
    cp = {'Νομός Αθηνών':'Αθήνα','Νομός Ανατολικής Αττικής':'Παλλήνη','Νομός Δυτικής Αττικής':'Ελευσίνα',
          'Νομός Πειραιά':'Πειραιάς','Νομός Ευβοίας':'Χαλκίδα'}
    return cp


main()