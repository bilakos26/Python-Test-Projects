agoria = int(input('Δώσε τον αριθμό των αγοριών της τάξης: '))
koritsia = int(input('Δώσε τον αριθμό των κοριτσιών της τάξης: '))
synolo = int(agoria + koritsia)
pososto_ag = float(agoria / synolo)
pososto_ko = float(koritsia / synolo)
print('Από ένα σύνολο', synolo, 'παιδιών, τα ποσοστά είναι τα εξής:',
      '\nΑγόρια:', format(pososto_ag, '.0%'), '\nΚορίτσια:',
      format(pososto_ko, '.0%'), sep=' ')
