#Οι ονομασίες προέρχονται από μία εργασία στο Insomnia.
#Οι αριθμοί είναι τυχαίοι για το τεστ του αρχείου
#Το ζητούμενο είναι να εμφανιστεί με ακρίβεια το 3ο δεκαδικό ψηφίο χωρίς να γίνει στρογγυλοποίηση σε αυτό

import math 

mesos_oros = 1.2365684
apoklisi = 1.3659465

print(math.floor(mesos_oros* 10 ** 3) / 10 ** 3)
print(math.floor(apoklisi* 10 ** 3) / 10 ** 3)
print()

#3o δεκαδικό για τον Μέσο Όρο
list_average = str(mesos_oros)
index_list_avg = list_average.index(".")
print(index_list_avg)
list_average = list_average[:index_list_avg + 4]

#3ο δεκαδικό για την Τυπική Απόκλιση
list_apoklisi = str(apoklisi)
index_list_apoklisi = list_apoklisi.index(".")
print(index_list_apoklisi)
list_apoklisi = list_apoklisi[:index_list_apoklisi + 4]

with open("outputdata.txt",'w') as out:
    out.write(f"Μέσος όρος = {list_average}" + "\n")    
    out.write(f"Τυπική απόκλιση = {list_apoklisi}" + "\n")