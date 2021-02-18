def EisodosDefterolepton():
    question = int(input('Πόσα βίντεο έχεις; '))
    seconds_file = open(r'C:\Users\bilakos\Desktop\PYTHON_TEST\test\video_seconds.txt', 'a')
    print('Δώσε τι χρονική διάρκεια για κάθε βίντεο.')
    for i in range(1, question + 1):
        seconds = float(input('Βίντεο #' + str(i) + ': '))
        seconds_file.write(str(seconds) + '\n')
    seconds_file.close()
    print('Οι χρόνοι αποθηκεύτηκαν στο αρχείο video_seconds.txt')


EisodosDefterolepton()