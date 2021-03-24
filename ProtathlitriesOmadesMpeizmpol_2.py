def main():
    team = load_teams()
    tm1, tm2 = team_wins(team)
    year_question(tm1, tm2)


def load_teams():
    team_l = []
    with open(r'C:\Users\bilakos\Desktop\ΠΡΟΓΡΑΜΜΑΤΑ & ΑΡΧΕΙΑ ΑΠΟ ΤΟ ΒΙΒΛΙΟ ΞΕΚΙΝΩΝΤΑΣ ΜΕ ΤΗΝ PYHTON\gaddis_python3_sourcecode\gaddis_python3_sourcecode\Chapter 07\WorldSeriesWinners.txt', 'r') as f_team:
        team = f_team.readline()
        while team != '':
            team = team.rstrip('\n')
            team_l.append(team)
            team = f_team.readline()
    return team_l


def team_wins(team):
    tm = {}
    tm2 = {}
    for t in team:
        tm[t] = team.count(t)
    counter = 1903
    for t2 in team:
        if counter == 1904:
            counter += 1
            tm2[counter] = t2
        elif counter == 1994:
            counter += 1
            tm2[counter] = t2
        else:
           tm2[counter] = t2
        counter += 1
    return tm, tm2


def year_question(tm1, tm2):
    question = int(input("Δώσε σε το ετος ευρεσης για τις Πρωταθλήτριες Ομάδες Μπέιζμπολ από το 1903 έως το 2008 (π.χ. 1995): "))
    t2 = tm2.get(question, f'\nΔεν έγινε πρωτάθλημα το {question}.')
    t1 = tm1.get(t2)
    if question in tm2:
        print(f'Για το έτος {question}, το πρωτάθλημα το είχανε κερδίσει οι {t2}.\n')
        print(f'Η Πρωταθλήτρια Ομάδα του Μπέιζμπολ {t2}, έχει κερδίσει {t1} ', end='')
        if t1 > 1:
            print('πρωταθλήματα.')
        else:
            print('πρωτάθλημα.')
    else:
        print(t2) 


main()