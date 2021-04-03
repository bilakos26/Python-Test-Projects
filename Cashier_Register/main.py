import retail


def main():
    #Create your CashRegister object to store retail items
    cart = retail.CashRegister()

    descr = input("Enter the description of the item that you want to buy or C to clear the Cart list or Q to quit: ")
    while descr.lower() != 'q':
        if descr.lower() != 'c':
            quantity = int(input('Enter the quantity you did like to buy: '))
            price_per_unit = float(input('Enter the price for 1 of them: '))
            price = quantity * price_per_unit
            print()
            item = retail.RetailItem(descr, quantity, price)
            cart.purchase_item(item)
        else:
            cart.clear()

        descr = input("Enter the description of the item that you want to buy or C to clear the Cart list or Q to quit: ")

    print()
    cart.show_items()
    print()
    print(f'Your total ${cart.get_total()}')


main()