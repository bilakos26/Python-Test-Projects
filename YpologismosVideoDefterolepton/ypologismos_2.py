def ektelesi():
	seconds_file = open(r'C:\Users\bilakos\Desktop\PYTHON_TEST\test\video_seconds.txt', 'r')
	total = 0.0
	count = 0
	line = seconds_file.readline()
	while line != '':
		seconds = float(line)
		count += 1
		print('Βίντεο #', count, ': ', seconds, sep='')
		total += seconds
		line = seconds_file.readline()
	seconds_file.close()
	print('Η συνολική διάρκεια είναι ', total, 'sec')
ektelesi()