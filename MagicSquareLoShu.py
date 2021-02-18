def main():
    numbers_entry = ekxorisi()
    ypologismos(numbers_entry)

def ekxorisi():
    lista = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    count = 1
    count2 = 0
    lista2 = []
    while count != 0 :
        for x in range(3):
            for y in range(3):
                arithmoi = input('Δώσε έναν αριθμό: ')
                lista2.append(arithmoi)
                if count == 1:
                    lista[x][y] = arithmoi
                    count += 1
                else:
                    times = 0
                    for i in lista2:
                        if i != arithmoi:
                            lista[x][y] = arithmoi
                            count = 0
                        else:
                            times += 1
                            print('Ο αριθμός που έδωσες υπάρχει ', times, ' φορές', sep='')
                            if times > 1:
                                count2 += 1
                    times = 0
        if count2 > 0:
            count = 1
            lista = [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]
            lista2 = []
            count2 = 0
            print('Ορισμένοι αριθμοί που βάλατε υπήρχανε περισσότερες από μια φορές στην λίστα με τους αριθμούς'
                ' δώσατε.')
            print('Ξανά δώστε τους αριθμούς για να δημιουργήσετε ένα πίνακα Lo Shu.')
        else:
            print(lista)
            print(lista2)
    return lista


def ypologismos(numbers_entry):
    logiki_timi = True
    count1 = 0
    #Υπολογισμός κάθε στήλης να είναι ίση με το 15
    
    for x in range(3):
        while logiki_timi == True:    
            for y in range(3):
                r = numbers_entry[x][y]
                r = int(r)
                count1 += r
            if count1 != 15:
                logiki_timi = False
    print(count1)

    #Υπολογισμός κάθε γραμμής να είναι ίση με το 15
    while logiki_timi == True:
        count2 = 0       
        for x in range(3):
            while logiki_timi == True:    
                for y in range(3):
                    r = numbers_entry[y][x]
                    r = int(r)
                    count2 += r
                if count2 != 15:
                    logiki_timi = False
        print(count2)

    #Υπολογισμός διαγωνίου1
    while logiki_timi == True:
        count3 = 0     
        for x in range(3):
            print('x= ', x)
            r = numbers_entry[x][x]
            r = int(r)
            count3 += r
        print(count3)

    #Υπολογισμός διαγωνίου2
    while logiki_timi == True:
        count4 = 0
        y = 2     
        for x in range(3):
            print('x= ', x)
            r = numbers_entry[y][x]
            r = int(r)
            count4 += r
            y -= 1
        print(count4)
    if count1 == 45 and count2 == 45 and count3 == 15 and count4 == 15:
        print('Η λίστα των αριθμών που εισάγατε είναι ένα Μαγικό Τετράγωνο Lo Shu.')
    else:
        print('Η λίστα των αριθμών που εισάγατε δεν είναι ένα Μαγικό Τετράγωνο Lo Shu.')


main()