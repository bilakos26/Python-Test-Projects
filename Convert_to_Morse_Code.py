def main():
    string = string_entry()
    alphabet_list = alphabet()
    convertion_to_Morse(string, alphabet_list)

def alphabet():
    alphabet_list = [' = ', ',=--..--', '.=.-.-.-', '?=..--..', ';=..--..', ':=---...', '"=.-..-.',
                     "(=-.--.", ")=-.--.-", '/=-..-.', '0=-----', '1=.----', '2=..---', '3=...--',
                     '4=....-', '5=.....', '6=-....', '7=--...', '8=---..', '9=----.', 'A=.-', 'B=-...',
                     'C=-.-.', 'D=-..', 'E=.', 'F=..-.', 'G=--.', 'H=....', 'I=..', 'J=.---', 'K=-.-',
                     'L=.-..', 'M=--', 'N=-.', 'O=---', 'P=.--.', 'Q=--.-', 'R=.-.', 'S=...', 'T=-',
                     'U=..-', 'V=...-', 'W=.--', 'X=-..-', 'Y=-.-', 'Z=--..', 'Α=.-', 'Β=-...',
                     'Θ=-.-.', 'Δ=-..', 'Ε=.', 'Φ=..-.', 'Γ=--.', 'Η=....', 'Ι=..', 'Κ=-.-',
                     'Λ=.-..', 'Μ=--', 'Ν=-.', 'Ο=---', 'Π=.--.', 'Ψ=--.-', 'Ρ=.-.', 'Σ=...', 'Τ=-',
                     'Ω=.--', 'Ξ=-..-', 'Υ=-.-', 'Ζ=--..', 'Χ=----']
    return alphabet_list


def string_entry():
    string = str(input("Δώσε ένα κείμενο γραμμένο στα Ελληνικά (χωρίς τόνους) ή στα Αγγλικά: "))
    return string


def convertion_to_Morse(string, alphabet_list):
    string = string.upper()
    word = ''
    for st in string:
        for al in alphabet_list:
            if st == al[0]:
                word = word + al[2:]
    print(word)

main()