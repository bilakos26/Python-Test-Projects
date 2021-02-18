import random


def main():
    ran_nums = random_numbers()
    emfanisi_periexomenou(ran_nums)

def random_numbers():
    num = []
    for i in range(1, 8):
        random_num = random.randint(0, 9)
        num.append(random_num)
    return num


def emfanisi_periexomenou(ran_nums):
    print('Ο αριθμός λαχείου είναι: ', end='')
    for i in ran_nums:
        print(i, end='')
    
main()