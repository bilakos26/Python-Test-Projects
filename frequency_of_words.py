def main():
    words = load_file()
    unique_wd1(words)
    unique_wd2(words)


def load_file():
	with open("name.txt", 'r') as lf:
		n = lf.read()
	return n

#Solution 12
#This is working better than the Solution 2. 
def unique_wd1(words):
    fr = {}
    words = words.lower()
    words = words.split()
    for wd in words:
        for i in wd:
            if i == ' ' or i == '.' or i == '' or i == ',' or i == '!' or i == '?' or i == ':':
                wd_ = words.index(wd)
                wd = wd.strip(i)
                words[wd_] = wd
        #UPPER = words.count(wd.upper())
        #LOWER = words.count(wd.lower())
        #wd = wd[0].upper() + wd[1:]
        #FIRST_UPPER = words.count(wd)
        #fr[wd] = (UPPER + LOWER + FIRST_UPPER)
        fr[wd] = words.count(wd)
    print(fr)

#Solution 2
def unique_wd2(words):
    wd = ''
    fr = {}
    wd_list = []
    count = 0
    len_w = len(words)
    for i in words:
        if i != ' ' and i != '.' and count != len_w and i != '' and i != ',' and i != '!' and i != '?' and i != ':':
            wd = wd + i
            count += 1
        else:
            count += 1
            if count == len_w:
                WD = wd
                print(WD)
                if WD != '':
                    WD = WD.strip('\n')
                    wd_list.append(WD)
                wd = ''
            WD = wd
            if WD != '':
                WD = WD.strip('\n')
                wd_list.append(WD)
            wd = ''
    for i in wd_list:
        #i = i.strip('\n')
        counter = wd_list.count(i)
        fr[i] = counter
    print(fr)


main()