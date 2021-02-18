import os

def main():
    correct_answers = sostes_apantiseis()
    apantiseis_eksetazomenou()
    vatmologia(correct_answers)

def sostes_apantiseis():
    correct_answers = ['1.Α', '2.Γ', '3.Α', '4.Α', '5.Δ', '6.Β', '7.Γ', '8.Α', '9.Γ', '10.Β', '11.Α', '12.Δ', 
                       '13.Γ', '14.Α', '15.Δ', '16.Γ', '17.Β', '18.Β', '19.Δ', '20.Α']
    return correct_answers

def apantiseis_eksetazomenou():
    arxeio = open(r'C:\Users\bilakos\Desktop\PYTHON_PROJECTS\PYTHON_TEST\PROGRAMMA_EKSETASIS_DIPLOMATOS_ODIGISIS\apantiseis.txt', 'a')
    print('Δώσε τις απαντήσεις του εξεταζομένου')
    count = 0
    for i in range(20):
        count += 1
        arxeio.write(str(count) + '.')
        print('Ερώτηση ', count, end='')
        apantisi = input(':')
        arxeio.write(apantisi + '\n')
    arxeio.close()

def vatmologia(correct_answers):
    arxeio = open(r'C:\Users\bilakos\Desktop\PYTHON_PROJECTS\PYTHON_TEST\PROGRAMMA_EKSETASIS_DIPLOMATOS_ODIGISIS\apantiseis.txt', 'r')
    cor_an = 0
    false_an = 0
    lista = []
    for i in arxeio:
        i = i.rstrip('\n')
        print(i)
        if i in correct_answers:
            cor_an += 1
        else:
            false_an += 1
            lista.append(i)
    arxeio.close()
    if cor_an >= 15:
        print('Ο εξεταζόμενος ΠΕΡΑΣΕ στη γραπτή εξέταση.')
    else:
        print('Ο εξταζόμενος ΑΠΕΤΥΧΕ στη γραπτή εξέταση.')
    print('Σωστές απαντήσεις: ', cor_an)
    print('Λανθασμένες απαντήσεις: ', false_an)
    print('Οι απαντήσεις των ερωτήσεων που έδωσες λάθος είναι οι εξής: ', lista)
    
    os.remove(r'C:\Users\bilakos\Desktop\PYTHON_PROJECTS\PYTHON_TEST\PROGRAMMA_EKSETASIS_DIPLOMATOS_ODIGISIS\apantiseis.txt')


main()