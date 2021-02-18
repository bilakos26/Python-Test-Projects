# Το εμβαδόν ενός ορθογωνίου ισούται με το μήκος επί το πλάτος του.
orth1_m = float(input('Δώσε το μήκος του 1ου ορθογωνίου: '))
orth1_p = float(input('Δώσε το πλάτος του 1ου ορθογωνίου: '))
orth2_m = float(input('Δώσε το μήκος του 2ου ορθογωνίου: '))
orth2_p = float(input('Δώσε το πλάτος του 2ου ορθογωνίου: '))
emvadon1 = orth1_m * orth1_p
emvadon2 = orth2_m * orth2_p
if emvadon1 > emvadon2:
    print('Το εμβαδόν του 1ου ορθογωνίου είναι μεγαλύτερο από αυτό του '
          '2ου:\nΕμβαδόν 1ου: ', format(emvadon1, ',.2f'),
          '\nΕμβαδόν 2ου: ', format(emvadon2, ',.2f'), sep='')
elif emvadon1 < emvadon2:
    print('Το εμβαδόν του 2ου ορθογωνίου είναι μεγαλύτερο από αυτό του '
          '1ου:\nΕμβαδόν 1ου: ', format(emvadon1, ',.2f'),
          '\nΕμβαδόν 2ου: ', format(emvadon2, ',.2f'), sep='')
else:
    print('Τα δύο ορθογώνια έχουν ίσο εμβαδόν:\nΕμβαδόν 1ου: ',
          format(emvadon1, ',.2f'),
          '\nΕμβαδόν 2ου: ', format(emvadon2, ',.2f'), sep='')
