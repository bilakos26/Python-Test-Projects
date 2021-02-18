def read_file():
    print('Αυτές είναι οι εγγραφές του αρχείου:')
    print()
    file_name = open(r'C:\Users\bilakos\Desktop\PYTHON_TEST\Score_sto_Golf\golf_stats.txt', 'r')
    name = file_name.readline()
    while name != '':
        score = file_name.readline()
        name = name.rstrip('\n')
        score = score.rstrip('\n')
        print('Όνοματεπώνυμο: ', name, sep='')
        print('Σκορ: ', score, sep='')
        print()
        name = file_name.readline()
    file_name.close()
