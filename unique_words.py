def main():
	words = load_file()
	unique_wd(words)


def load_file():
	with open("name.txt", 'r') as lf:
		n = lf.read()
	return n


def unique_wd(words):
	uw = set(words)
	wd = []
	for i in uw:
		if i != ' ':
			wd.append(i)
	print(wd)


main()