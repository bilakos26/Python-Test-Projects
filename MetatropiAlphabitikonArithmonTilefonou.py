def main():
    num = number()
    convert_num(num)

def convert_num(num):
    num = num.upper()
    phone_num = ''
    for nm in num:
        if nm == "A" or nm == 'B' or nm == 'C':
            phone_num = phone_num + '2'
        elif nm == 'D' or nm == 'E' or nm == 'F':
            phone_num = phone_num + '3'
        elif nm == 'G' or nm == 'H' or nm == 'I':
            phone_num = phone_num + '4'
        elif nm == 'J' or nm == 'K' or nm == 'L':
            phone_num = phone_num + '5'
        elif nm == 'M' or nm == 'N' or nm == 'O':
            phone_num = phone_num + '6'
        elif nm == 'P' or nm == 'Q' or nm == 'R' or nm == 'S':
            phone_num = phone_num + '7'
        elif nm == 'T' or nm == 'U' or nm == 'V':
            phone_num = phone_num + '8'
        elif nm == 'W' or nm == 'X' or nm == 'Y' or nm == 'Z':
            phone_num = phone_num + '9'
        else:
            phone_num = phone_num + nm 
    print(int(phone_num))

def number():
    num = input("Give a phone number with 10 digits: ")
    return num

main()