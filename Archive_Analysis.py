def main():
    words1, words2 = load_file()
    fr, fr2 =unique_wd1_2(words1, words2)
    words_contained_to_the_files(fr, fr2)
    sym_dif(fr, fr2)


def load_file():
	with open("word.txt", 'r') as lf:
		w1 = lf.read()
	with open("word2.txt", 'r') as lf2:
		w2 = lf2.read()	
	return w1, w2	


def unique_wd1_2(words1, words2):
    fr = set()
    fr2 = set()
    words1 = words1.lower()
    words1 = words1.split()
    for wd in words1:
        for i in wd:
            if i == ' ' or i == '.' or i == '' or i == ',' or i == '!' or i == '?' or i == ':':
                wd_ = words1.index(wd)
                wd = wd.strip(i)
                words1[wd_] = wd
        fr.update([wd])
    print(fr)
    words2 = words2.lower()
    words2 = words2.split()
    for wd in words2:
        for i in wd:
            if i == ' ' or i == '.' or i == '' or i == ',' or i == '!' or i == '?' or i == ':':
                wd_ = words2.index(wd)
                wd = wd.strip(i)
                words2[wd_] = wd
        fr2.update([wd])
    print(fr2)
    return fr, fr2


def words_contained_to_the_files(fr, fr2):
    words = set(fr)
    words.update(fr2)
    print(words)


def sym_dif(fr, fr2):
    set1 = set(fr)
    set2 = set(fr2)
    set3 = set1.symmetric_difference(set2)
    for i in set3:
        print(i)


main()