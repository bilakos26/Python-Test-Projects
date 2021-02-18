def main():
    word = pig_word()
    reverse_word(word)


def reverse_word(word):
    final_word = ''
    space = 0
    count = 0
    for i in word:
        if space == 0:
            first_word = i + 'AY '
            space += 1
            count += 1
        else:
            if i.isspace():
                final_word = final_word + first_word
                space = 0
                count += 1
            else:
                final_word = final_word + i
                count += 1
            if len(word) == count:
                final_word = final_word + first_word
    print(final_word)


def pig_word():
    word = input('Give a sentence: ')
    word = word.upper()
    return word


main()