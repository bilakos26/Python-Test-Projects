blue = 'Μπλέ'
red = 'Κόκκινο'
yellow = 'Κίτρινο'
print('Τα βασικά χρώματα είναι το Κόκκινο, το Μπλέ και το Κίτρινο.')
eisodos1 = input('Δώσε το 1ο βασικό χρώμα για ανάμειξη: ')
eisodos2 = input('Δώσε το 2ο βασικό χρώμα για ανάμειξη: ')
if eisodos1 == red and eisodos2 == blue:
    print('Με την ανάμειξη των βασικών αυτών χρωμάτων προκύπτει το Μωβ.')
elif eisodos1 == red and eisodos2 == yellow:
    print('Με την ανάμειξη των βασικών αυτών χρωμάτων προκύπτει το Πορτοκαλί.')
elif eisodos1 == blue and eisodos2 == yellow:
    print('Με την ανάμειξη των βασικών αυτών χρωμάτων προκύπτει το Πράσινο.')
else:
    print('Έχετε δώσει διαφορετικό χρώμα από τα βασικά χρώματα.')