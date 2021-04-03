class RetailItem:
    def __init__(self, description, num_units, price):
        self.__descr = description
        self.__qty = num_units
        self.__price = price

    
    def set_description(self, description):
        self.__descr = description


    def set_quantity(self, num_units):
        self.__qty = num_units


    def set_price(self, price):
        self.__price = price


    def get_description(self):
        return self.__descr


    def get_quantity(self):
        return self.__qty


    def get_price(self):
        return self.__price


    def __str__(self):
        return (
            """
            Description: %s
            Quantity: %s
            Product Price: $%s
            """%(
                self.__descr, self.__qty,
                format(self.__price, ',.2f')
            )
        )


class CashRegister:
    #Εδώ δημιουργούμε ένα αντικείμενο με μια άδεια λίστα για το καλάθι. Είναι το σημείο
    #στο οποίο θα μπαίνουν τα προϊόντα
    def __init__(self):
        self.__cart = []


    def purchase_item(self, item):
        #Create a list of all the descriptions of the items, that is already in the cart
        cart_description = []
        for retail_item in self.__cart:
            cart_description.append(retail_item.get_description())
        
        #If the purchased item isn't already in the cart, then just add it in
        if item.get_description() not in cart_description:
            self.__cart.append(item)
        #Otherwise we have to find it in the cart and update the quantity and price
        else:
            for i in range(len(self.__cart)):
                if item.get_description() == self.__cart[i].get_description():
                    #self.__cart[i].get_quantity() + item.set_quantity() --> Αυτό το κάνουμε γιατί η περιγραγή του προϊόντος(description) 
                    #της item βρίσκεται ήδη μέσα στη λίστα της self.__cart , οπότε θέλουμε να ανανεώσουμε την ποσότητα και την τιμή
                    # από το προϊόν που ήδη υπάρχει μέσα στην λίστα. Για τον λόγο αυτό καλούμε την self.__cart[i].get_quantity() όπου βρίσκεται
                    # αποθηκευμένη η ποσότητα του προϊόντος και έπειτα καλούμε την item.set_quantity() για να προσθέσει την προηγούμενη
                    # ποσότητα με την νέα και να έχουμε σαν αποτέλεσμα, την νέα ποσότητα του προϊόντος. 
                    self.__cart[i].set_quantity(self.__cart[i].get_quantity() + item.set_quantity())
                    self.__cart[i].set_price(self.__cart[i].get_price() + item.set_price())
    

    def get_total(self):
        total = 0
        for item in self.__cart:
            total += item.get_price()
        return format(total, ',.2f')


    def show_items(self):
        print("\t------- YOUR CART -------")
        print()
        for item in self.__cart:
            #Εμφανίζει τα αντικείμενα, της μεθόδου __str__ , στην κλάση RetailItem
            print(item)
            print('\t-------------------------')
            

    
    def clear(self):
        self.__cart = []