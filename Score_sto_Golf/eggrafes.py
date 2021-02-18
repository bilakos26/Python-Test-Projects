import EmfanisiEggrafon

def ektelesi():
    answer_1 = 'Y'
    while answer_1 == 'Y' or answer_1 == 'y':
        try:
            player_name = eisagogi_onomatos()
            player_score = eisagogi_score()
            EisagogiStoArxeio(player_name, player_score)
            answer_1 = input('Θέλεις να κάνεις άλλη καταχώρηση; Υ/y = ΝΑΙ, οτιδήποτε άλλο = ΌΧΙ: ')
            answer_2 = input('Θέλεις να εμφανίσεις τις καταχωρήσεις των εγγραφών; '
                             'Υ/y = ΝΑΙ, οτιδήποτε άλλο = ΌΧΙ: ')
            if answer_2 == 'Y' or answer_2 == 'y':
                EmfanisiEggrafon.read_file()
            else:
                print()
        except Exception as Error:
            print(Error)


def eisagogi_onomatos():
    onoma = input('Δώσε το ονοματεπώνυμο του παίκτη: ')
    print()
    return onoma


def eisagogi_score():
    score = input('Δώσε το σκορ του παίχτη: ')
    print()
    return score


def EisagogiStoArxeio(player_name, player_score):
    file_name = open(r'C:\Users\bilakos\Desktop\PYTHON_TEST\Score_sto_Golf\golf_stats.txt', 'a')
    file_name.write(player_name + '\n')
    file_name.write(player_score + '\n')
    file_name.close()
    print('Το αρχείο golf_stats.txt ενημερώθηκε.')
    print()

ektelesi()