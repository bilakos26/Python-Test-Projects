import defterolepta


def ektelesi():
	defterolepta.EisodosDefterolepton()
	ypologismos_defterolepton()


def ypologismos_defterolepton():
	seconds_file = open(r'C:\Users\bilakos\Desktop\PYTHON_TEST\test\video_seconds.txt', 'r')
	total = 0.0
	count = 0
	print('Η χρονική διάρκεια κάθε βίντεο είναι:')
	for i in seconds_file:
		seconds = float(i)
		count += 1
		print('Βίντεο #', count, ': ', seconds, sep='')
		total += seconds
	seconds_file.close()

	print('Η συνολική διάρκεια είναι ', total, 'sec')


ektelesi()