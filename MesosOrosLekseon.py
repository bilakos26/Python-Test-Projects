with open(r'C:\Users\bilakos\Desktop\ΠΡΟΓΡΑΜΜΑΤΑ & ΑΡΧΕΙΑ ΑΠΟ ΤΟ ΒΙΒΛΙΟ ΞΕΚΙΝΩΝΤΑΣ ΜΕ ΤΗΝ PYHTON\gaddis_python3_sourcecode\gaddis_python3_sourcecode\Chapter 08\text.txt', 'r') as txt_file:
    words = txt_file.readline()
    count = 0
    while words != '':
        for i in words:
            if i.isspace():
                count += 1
            else:
                continue
        words = txt_file.readline()
print(count)