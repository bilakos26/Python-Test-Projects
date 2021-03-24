import random
from time import sleep

def main():
    deck = create_deck()
    simulation(deck)


def create_deck():
    deck = {'Άσος Μπαστούνι':11, '2 Μπαστούνι':2, '3 Μπαστούνι':3, '4 Μπαστούνι':4, '5 Μπαστούνι':5,
            '6 Μπαστούνι':6, '7 Μπαστούνι':7, '8 Μπαστούνι':8, '9 Μπαστούνι':9, '10 Μπαστούνι':10,
            'Βαλές Μπαστούνι':10, 'Ντάμα Μπαστούνι':10, 'Ρήγας Μπαστούνι':10,
            
            'Άσος Κούπα':11, '2 Κούπα':2, '3 Κούπα':3, '4 Κούπα':4, '5 Κούπα':5,
            '6 Κούπα':6, '7 Κούπα':7, '8 Κούπα':8, '9 Κούπα':9, '10 Κούπα':10,
            'Βαλές Κούπα':10, 'Ντάμα Κούπα':10, 'Ρήγας Κούπα':10,
            
            'Άσος Σπαθί':11, '2 Σπαθί':2, '3 Σπαθί':3, '4 Σπαθί':4, '5 Σπαθί':5,
            '6 Σπαθί':6, '7 Σπαθί':7, '8 Σπαθί':8, '9 Σπαθί':9, '10 Σπαθί':10,
            'Βαλές Σπαθί':10, 'Ντάμα Σπαθί':10, 'Ρήγας Σπαθί':10,
            
            'Άσος Καρό':11, '2 Καρό':2, '3 Καρό':3, '4 Καρό':4, '5 Καρό':5,
            '6 Καρό':6, '7 Καρό':7, '8 Καρό':8, '9 Καρό':9, '10 Καρό':10,
            'Βαλές Καρό':10, 'Ντάμα Καρό':10, 'Ρήγας Καρό':10}
    return deck


def simulation(deck):
    p1 = {}
    p2 = {}
    value1 = 0
    value2 = 0
    len_d = len(deck)
    hand_value1 = 0
    hand_value2 = 0
    card1 = ''
    card2 = ''
    count = 0
    question1 = True
    question2 = True
    while count != len_d or True:
        if question1 == True:
            count += 1
            pl1 = player1(hand_value1, p1)
            if pl1 == 'Ν' or pl1 == 'ν':    
                card1, value1 = random.choice(list(deck.items())) #Η μέθοδος popitem() έπερνε πάντα το τελευταίο στοιχείο της λίστας πράγμα που την καθιστά προκαθορισμένη.
                print(card1)
                if 'Άσος' in card1:
                    if hand_value1 > 11:
                        hand_value1 += 1
                    else:
                        hand_value1 += value1
                else:
                    hand_value1 += value1
                print('Άθροισμα φύλλων ΠΑΙΚΤΗ 1: ', hand_value1, '\n')
                del deck[card1]
            else:
                question1 = False
        
        p1[card1] = value1

        if hand_value1 == 21:
            print(f'Ο ΠΑΙΚΤΗΣ 1 κέρδισε με άθροισμα φύλλων: {hand_value1}.')
            print(f'\nΟ ΠΑΙΚΤΗΣ 2 έχασε, με άθροισμα φύλλων: {hand_value2}.')
            break
        elif hand_value1 > 21:
            print(f'Ο ΠΑΙΚΤΗΣ 1 έχασε, με άθροισμα φύλλων: {hand_value1}.')
            print(f'\nΟ ΠΑΙΚΤΗΣ 2 κέρδισε με άθροισμα φύλλων: {hand_value2}.')
            break
        
        if question2 == True:
            count += 1
            pl2 = player2(hand_value2, p2)
            if pl2 == 'Ν' or pl2 == 'ν':    
                card2, value2 = random.choice(list(deck.items())) #Η μέθοδος popitem() έπερνε πάντα το τελευταίο στοιχείο της λίστας πράγμα που την καθιστά προκαθορισμένη.
                print(card2)
                if 'Άσος' in card2:
                    if hand_value2 > 11:
                        hand_value2 += 1
                    else:
                        hand_value2 += value2
                else:
                    hand_value2 += value2
                print('Άθροισμα φύλλων ΠΑΙΚΤΗ 2: ', hand_value2, '\n')
                del deck[card2]
            else:
                question2 = False
        
        p2[card2] = value2

        if hand_value2 == 21:
            print(f'Ο ΠΑΙΚΤΗΣ 2 κέρδισε με άθροισμα φύλλων: {hand_value2}.')
            print(f'\nΟ ΠΑΙΚΤΗΣ 1 έχασε, με άθροισμα φύλλων: {hand_value1}.')
            break
        elif hand_value2 > 21:
            print(f'Ο ΠΑΙΚΤΗΣ 2 έχασε, με άθροισμα φύλλων: {hand_value2}.')
            print(f'\nΟ ΠΑΙΚΤΗΣ 1 κέρδισε με άθροισμα φύλλων: {hand_value1}.')
            break
        
        if hand_value1 >= 21 and hand_value2 >= 21:
            print(f'Κανείς από τους δύο παίκτες δεν κερδίζει.\nΠΑΙΚΤΗΣ 1 άθροισμα φύλλων: {hand_value1}\nΠΑΙΚΤΗΣ 2 άθροισμα φύλλων: {hand_value2}')
            break
        elif question1 == True and question2 == True:
            continue
        elif question1 == False and question2 == True:
            if hand_value2 > hand_value1:
                print(f'Ο ΠΑΙΚΤΗΣ 2 κέρδισε με άθροισμα φύλλων: {hand_value2}.')
                print(f'\nΟ ΠΑΙΚΤΗΣ 1 έχασε, με άθροισμα φύλλων: {hand_value1}.')
                break
            else:
                continue
        elif question1 == True and question2 == False:
            if hand_value1 > hand_value2:
                print(f'Ο ΠΑΙΚΤΗΣ 1 κέρδισε με άθροισμα φύλλων: {hand_value1}.')
                print(f'\nΟ ΠΑΙΚΤΗΣ 2 έχασε, με άθροισμα φύλλων: {hand_value2}.')
                break
            else:
                continue
        elif question1 == False and question2 == False:
            if hand_value1 == hand_value2:
                print(f'Κανείς από τους δύο παίκτες δεν κερδίζει, γιατί έχουν το ίδιο άθροισμα φύλλων: {hand_value1}.')
                break 
            elif hand_value1 > hand_value2:
                print(f'Ο ΠΑΙΚΤΗΣ 1 κέρδισε με άθροισμα φύλλων: {hand_value1}.')
                print(f'\nΟ ΠΑΙΚΤΗΣ 2 έχασε, με άθροισμα φύλλων: {hand_value2}.')
                break
            else:
                print(f'Ο ΠΑΙΚΤΗΣ 2 κέρδισε με άθροισμα φύλλων: {hand_value2}.')
                print(f'\nΟ ΠΑΙΚΤΗΣ 1 έχασε, με άθροισμα φύλλων: {hand_value1}.')
                break

    sleep(10)


def player1(hand_value1, p1):
    print('--- Προηγούμενα φύλλα ΠΑΙΚΤΗ 1 ---\n')
    for k, v in p1.items():
        print(k, ' = ', v)
    print(f'Άθροισμα Φύλλων: {hand_value1}\n')
    question = input('--- ΠΑΙΚΤΗΣ 1 ---\nΘέλεις να τραβήξεις φύλλο;\nΔώσε Ν/ν για ΝΑΙ. Οτιδήποτε άλλο = ΟΧΙ : ')
    print('\n')
    return question


def player2(hand_value2, p2):
    print('--- Προηγούμενα φύλλα ΠΑΙΚΤΗ 2 ---\n')
    for k, v in p2.items():
        print(k, ' = ', v)
    print(f'Άθροισμα Φύλλων: {hand_value2}\n')
    question = input(f'--- ΠΑΙΚΤΗΣ 2 ---\nΘέλεις να τραβήξεις φύλλο;\nΔώσε Ν/ν για ΝΑΙ. Οτιδήποτε άλλο = ΟΧΙ : ')
    print('\n')
    return question             


main()