def ektelesi():
	try:
		name_search = eisagogi_anazitisis()
		counter = metritis_grammon(name_search)
		emfanisi_arxeiou(name_search, counter)
	except Exception as Error:
		print('Το όνομα του αρχείου που δώσατε δεν υπάρχει.\n', Error)


def eisagogi_anazitisis():
	anazitisi = input('Δώσε το όνομα του αρχείου: ')
	print()
	return anazitisi


def metritis_grammon(name_search):
	file_name = open(r'C:\Users\bilakos\Desktop\PYTHON_TEST\EmfanisiArxeiou' + '\\' + name_search, 'r')
	arxeio = file_name.readline()
	y = 0
	while arxeio != '':
		y += 1 
		arxeio = file_name.readline()
	file_name.close()
	return y


def emfanisi_arxeiou(name_search, counter):
	file_name = open(r'C:\Users\bilakos\Desktop\PYTHON_TEST\EmfanisiArxeiou' + '\\' + name_search, 'r')
	print('Οι γραμμές είναι: ', counter)
	print()
	if counter >= 5:
		y = 0
		total = 0
		arxeio2 = file_name.readline()
		while y != 5:
			y += 1
			total += float(arxeio2)
			arxeio2 = arxeio2.rstrip('\n')
			print('#', y, ': ', str(arxeio2), sep='')
			arxeio2 = file_name.readline()
		print('Το άθροισμα είναι: ', total)
		print('Ο Μέσος Όρος των αριθμών είναι: ', (total/counter))
	else:
		total = 0
		y = 0
		print('Επειδή το αρχείο περιέχει λιγότερες απο πέντε γραμμές, το περιεχόμενο του αρχείου '
		      'είναι:\n')
		for i in file_name:
			num = int(i)
			y += 1
			total += num
			print('#', y, ': ', num, sep='')
		print('Το άθροισμα είναι: ', total)
		print('Ο Μέσος Όρος των αριθμών είναι: ', (total/counter))


ektelesi()