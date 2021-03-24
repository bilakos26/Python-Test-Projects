#Ο παρακάτω κώδικας δημιουργεί ένα κείμενο σε κώδικα Morse. Υπάρχει παρόμοιος κώδικας αλλα σε λίστα και όχι σε λεξικό με την ονομασία
#Convert_to_Morse_Code.py
import pickle

def main():
    string = string_entry()
    alphabet_list = alphabet()
    convertion_to_Morse(string, alphabet_list)
    decryption_Morse(alphabet_list)


def alphabet():
    alphabet_list = {' ':' ', ',':'--..--', '.':'.-.-.-', '?':'..--..', ';':'..--..', ':':'---...', '"':'.-..-.',
                     "(":"-.--.", ")":"-.--.-", '/':'-..-.', '0':'-----', '1':'.----', '2':'..---', '3':'...--',
                     '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', 'A':'.-', 'B':'-...',
                     'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-',
                     'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-',
                     'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..'}
    return alphabet_list


def string_entry():
    with open(r'C:\Users\bilakos\Desktop\PYTHON_PROJECTS\name.txt', 'r') as s_file:
        string = s_file.read()
    return string


def convertion_to_Morse(string, alphabet_list):
    string = string.upper()
    word = []
    for st in string:
        for al, vl in alphabet_list.items():
            if st == al:
                word.append(vl)
    with open('Morse.dat', 'wb') as m_file:
        pickle.dump(word, m_file)
    word_ = ''
    for i in word:
        word_ = word_ + i
    print(word_)


def decryption_Morse(alphabet_list):
    with open('Morse.dat', 'rb') as m_file:
        mor = pickle.load(m_file)
        word = ""
        for i in mor:
            for al in alphabet_list:
                if alphabet_list[al] == i:
                    word = word + al
        print(word)


main()