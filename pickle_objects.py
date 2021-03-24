import pickle

def main():
    again = "ν"
    end = False
    personal_f = open("personal.dat", "wb") #ή θα μπορουσα να το αλλαξω σε "ab"
    while again == "ν":
        save_data(personal_f)
        again = input("Είσοδος άλλων δεδομένων; (ν/ο): ")
        print(""*2)
    personal_f.close()
    #Αναγνωση αρχείου σειριοποιημενων αντικειμενων
    with open("personal.dat", "rb") as r_personal:
        while not end:
            try:
                r_p = pickle.load(r_personal)
                load_data(r_p)
            except Exception:
                end = True
        



def load_data(r_p):
    print("Name: ", r_p["name"])
    print("Age: ", r_p['age'])
    print("Weight: ", r_p["weight"])
    print('')


def save_data(personal_f):
    personal = {}
    personal['name'] = input("Δώσε Όνομα: ")
    personal['age'] = input("Δώσε Ηλικία: ")
    personal['weight'] = input("Δώσε Βάρος: ")
    print(''*2)
    print(personal)
    print("")
    #Αποθηκευση σειριοποιημενων αντικειμενων
    pickle.dump(personal, personal_f)

main()