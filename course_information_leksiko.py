#Το πρόγραμμα δημιουργεί ένα λεξικό με κωδικούς μαθημάτων και τους αριθμούς των αιθουσών στις οποίες διδάσκονται
#τα μαθήματα αυτά.

def main():
    sub_code = input("Δώσε τον κωδικό του μαθήματος: ")
    if sub_code in class_num() and sub_code in instructor() and sub_code in teaching_time(): 
        print('Αίθουσα: ', class_num()[sub_code], "\nΔιδάσκων: ", instructor()[sub_code],
        "\nΏρα μαθήματος: ", teaching_time()[sub_code], sep='')
    else:
        while sub_code not in class_num() and sub_code not in instructor() and sub_code not in teaching_time():
            print('Λανθασμένος κωδικός μαθήματος. Ξανά προσπάθησε.')
            sub_code = input("Δώσε τον κωδικό του μαθήματος: ")
        print('Αίθουσα: ', class_num()[sub_code], "\nΔιδάσκων: ", instructor()[sub_code],
        "\nΏρα μαθήματος: ", teaching_time()[sub_code], sep='')


def class_num():
    cl_n = {'CS101':'3004', 'CS102':'4501', 'CS103':'6755', 'NT110':'1244', 'CM241':'1411'}
    return cl_n


def instructor():
    ins = {'CS101':'Hayes', 'CS102':'Alvarado', 'CS103':'Rich', 'NT110':'Burke', 'CM241':'Lee'}
    return ins


def teaching_time():
    tc_t = {'CS101':'8:00 π.μ.', 'CS102':'9:00 π.μ.', 'CS103':'10:00 π.μ.', 'NT110':'11:00 π.μ.', 'CM241':'1:00 μ.μ.'}
    return tc_t


main()