import os

def main():
    numbers = arithmoi()
    epeksergasia_dedomenon(numbers)

def arithmoi():
    print('Το πρόγραμμα θα σου ζητήσει 20 φορές να του δώσεις έναν αριθμό.')
    print()
    count = 0
    nums = []
    for i in range(20):
        count += 1
        print('#', count, sep='', end='')
        arithmoi = float(input(' Δώσε έναν αριθμό: '))
        nums.append(arithmoi)
        print()
    return nums

def epeksergasia_dedomenon(numbers):
    synolo = 0
    for x in numbers:
        synolo += x
    min_num = min(numbers)
    max_num = max(numbers)
    average = synolo / len(numbers)
    print('Ο μικρότερος αριθμός είναι: ', min_num, '\nΟ μεγαλύτερος αριθμός είναι: ', max_num,
          '\nΤο άθροισμα των αριθμών είναι: ', synolo, '\nΟ μέσος όρος των αριθμών είναι: ', average, sep='')   

main()