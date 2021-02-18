def main():
    print("Δώσε το ονοματεπώνυμό σου σε λατινικούς χαρακτήρες π.χ. Vasilis και τον αριθμό μητρώου σου.")
    f_name = str(input("Δώσε το όνομα: "))
    l_name = str(input("Δώσε το επίθετο: "))
    am = str(input("Δώσε τον Αριθμό Μητρώου: "))
    
    FN = f_name[0:3]
    LN = l_name[0:3]
    AM = am[0:3]
    username = FN + LN + AM
    print(username)
    

main()