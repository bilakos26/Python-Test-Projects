# Το τελικό αποτέσμα στο συγκεκριμένο πρόβλημα για να έχει λογική προϋποθέτει
# την πώληση όλου του αριθμού των αγορασμένων μετοχών
def ektelesi():
    stocks_number = arithmos_metoxon()
    stock_price = timi_metoxis()
    SoldStocks = poulimenes_metoxes()
    SoldPrice = timi_polisis()
    commission = promitheia()
    # ΠΡΑΞΕΙΣ
    buy_amount = float(stocks_number * stock_price)  # ποσό αγοράς μετοχών
    buy_comm = float(buy_amount * commission)  # ποσο προμήθειας για αγορά
    sold_amount = float(SoldStocks * SoldPrice)  # ποσο πώλησης μετοχών
    sold_comm = float(sold_amount * commission)  # ποσο προμήθειας για πώληση
    print('Το ποσό των χρημάτων που πλήρωσες για τις μετοχές είναι: €',
          format(buy_amount, ',.2f'), sep='')
    print()
    print('Το ποσό της προμήθειας που πλήρωσες για την αγορά των μετοχών',
          ' είναι: €', format(buy_comm, ',.2f'), sep='')
    print()
    print('Το ποσό πώλησης των μετοχών είναι: €',
          format(sold_amount, ',.2f'), sep='')
    print()
    print('Το ποσό της προμήθειας που πλήρωσες για την πώληση των μετοχών',
          'είναι: €',
          format(sold_comm, ',.2f'), sep='')
    print()

    emeine_poso(sold_amount, sold_comm)  # το ποσο που έμεινε μετά την πώληση

# Εμφανίζει αν έχει κέρδος ή όχι
    kostos = buy_amount + buy_comm + sold_comm
    kerdos = sold_amount - kostos
    if sold_amount > kostos:
        print('Έβγαλες κέρδος: €', format(kerdos, ',.2f'), sep='')
    else:
        print('Έχασες λεφτά: €', format(kerdos, ',.2f'), sep='')
        print('Η πληρωμή του χρηματιστή και τις δυο φορές ήτανε:\n'
              '1η φορά: €', format(buy_comm, ',.2f'),
              '\n2η φορά: €', format(sold_comm, ',.2f'), sep='')
        print()


def arithmos_metoxon():
    stocks = float(input('Δώσε τον αριθμό των μετοχών που αγόρασες: '))
    print()
    return stocks


def timi_metoxis():
    price = float(input('Δώσε την τιμή της μετοχής ανά μονάδα που '
                        'αγόρασες: €'))
    print()
    return price


def poulimenes_metoxes():
    sold_stocks = float(input('Δώσε τον αριθμό των μετοχών που πούλησες: '))
    print()
    return sold_stocks


def timi_polisis():
    sold_price = float(input('Δώσε την τιμή πώλησης των μετοχών: €'))
    print()
    return sold_price


def promitheia():
    comm = float(input('Δώσε την προμήθεια που θα πρέπει να καταβάλεις '
                       'στον χρηματιστή: '))
    print()
    return comm


def emeine_poso(sold_amount, sold_comm):
    posoE = float(sold_amount - sold_comm)
    print('Το ποσό που σου έμεινε είναι: €', format(posoE, ',.2f'), sep='')


ektelesi()
