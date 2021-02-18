import getpass

def main():
    password = pass_insert()
    check_pass(password)


def pass_insert():
    #password = getpass.getpass("Create your password: ")
    password = str(input("Create your password: "))
    print("")
    #password2 = getpass.getpass("Confirm new password: ")
    password2 = str(input("Confirm new password: "))
    print(""*2)
    while password2 != password:
        print("You have made a mistake in your inputs.\n Please try again inserting your new password.\n")
        #password = getpass.getpass("Create your password: ")
        password = str(input("Create your password: "))
        print("")
        #password2 = str(input("Confirm new password: "))
        password2 = str(input("Confirm new password: "))
        print(""*2)
    return password


def pass_len(password):
    #STEP 1 --> Checking the lengt of the password to be at least 7 characters
    len_pass = len(password)
    while len_pass < 7:
        print("Wrong password.\nYou must insert at least 7 characters. Try again.")
        print('')
        len_pass = len(pass_insert())


def check_pass(password):
    pass_len(password)
    #STEP 2 --> Checking the password to contain at least 1 capital letter
    upper_validation = False
    lower_validation = False
    digit_validation = False
    for ck in password:
        if ck.isupper():
            upper_validation = True  
        if ck.islower():
            lower_validation = True
        if ck.isdigit():
            digit_validation = True
    if upper_validation == True and lower_validation == True and digit_validation == True:
        print(password)
    else:
        while upper_validation == False or lower_validation == False or digit_validation == False:
            print("Wrong password. The password must have 1 Capital, 1 Small and 1 Digit letter at least. Try again.")
            print("")
            upper_validation = False
            lower_validation = False
            digit_validation = False
            password = pass_insert()
            pass_len(password)
            for ck in password:
                if ck.isupper():
                    upper_validation = True 
                if ck.islower():
                    lower_validation = True
                if ck.isdigit():
                    digit_validation = True
        print(password)

main()