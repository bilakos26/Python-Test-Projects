F = float(input("Δώσε το επιθυμητό μελλοντικό ποσό:"))
r = float(input("Δώσε το ετήσιο επιτόκιο:"))
n = float(input("""Δώσε το πλήθος των ετών που θα παραμείνουν τα χρήματα στον
 λογαριασμό σου:"""))
p = float(F / ((1+r)**n))
print("Αυτό είναι το ποσό που πρέπει να κατατεθεί σήμερα: €",
      format(p, ",.2f"), sep='')