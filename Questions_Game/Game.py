class Question:

    def __init__(self, question, ans1, ans2, ans3, ans4, correct_ans):
        self.__ques = question
        self.__ans1 = ans1
        self.__ans2 = ans2
        self.__ans3 = ans3
        self.__ans4 = ans4
        self.__corr_ans = correct_ans


    def set_question(self, question):
        self.__ques = question

    def set_ans1(self, ans1):
        self.__ans1 = ans1
    
    def set_ans2(self, ans2):
        self.__ans2 = ans2

    def set_ans3(self, ans3):
        self.__ans3 = ans3

    def set_ans4(self, ans4):
        self.__ans4 = ans4

    def set_corr_ans(self, correct_ans):
        self.__corr_ans = correct_ans

    def get_question(self):
        return self.__ques

    def get_ans1(self):
        return self.__ans1

    def get_ans2(self):
        return self.__ans2

    def get_ans3(self):
        return self.__ans3

    def get_ans4(self):
        return self.__ans4
    
    def get_corr_ans(self):
        return self.__corr_ans

    def ask_question(self):
        print('Ερώτηση: '+ self.__ques +\
            '\n1.' + self.__ans1 +\
            '\n2.' + self.__ans2 +\
            '\n3.' + self.__ans3 +\
            '\n4.' + self.__ans4)

def questions_objs(row):
    i = row
    if i == 1:
        question = 'Πως σε λένε;'
        ans1 = 'Αχιλλέα'
        ans2 = 'Δημήτρη'
        ans3 = 'Βασίλη'
        ans4 = 'Γιώργο'
    elif i == 2:
        question = 'Τι χρώμα μαλλιών έχεις;'
        ans1 = 'Καστανό'
        ans2 = 'Μαύρο'
        ans3 = 'Τζίντζερ'
        ans4 = 'Ξανθό'
    elif i == 3:
        question = 'Πόσο ύψος έχεις;'
        ans1 = '1,70'
        ans2 = '1,85'
        ans3 = '1,90'
        ans4 = '1,83'
    elif i == 4:
        question = 'Τι χρώμα μάτια έχεις;'
        ans1 = 'Πράσινο'
        ans2 = 'Μαύρο'
        ans3 = 'Μπλέ'
        ans4 = 'Καστανό'
    elif i == 5:
        question = 'Πως ονομάζετε το κατοικίδιό σου;'
        ans1 = 'Max'
        ans2 = "Johnny's"
        ans3 = 'Wassabi'
        ans4 = 'Lila'
    elif i == 6:
        question = 'Ποιος είναι ο αριθμός του κινητού σου;'
        ans1 = '6941526788'
        ans2 = '6972865831'
        ans3 = '6981927488'
        ans4 = '6955623388'
    elif i == 7:
        question = 'Τι κινητό έχεις;'
        ans1 = 'Samsung'
        ans2 = 'Xiaomi'
        ans3 = 'LG'
        ans4 = 'Apple'
    elif i == 8:
        question = 'Ποιο είναι το αγαπημένο σου χόμπι;'
        ans1 = 'Μπάλα'
        ans2 = 'Μπάσκετ'
        ans3 = 'Αεροσφαίριση'
        ans4 = 'Τέννις'
    elif i == 9:
        question = 'Σε ποια πόλη ζεις;'
        ans1 = 'Τρίκαλα'
        ans2 = 'Λάρισα'
        ans3 = 'Καρδίτσα'
        ans4 = 'Βόλος'
    else:
        question = 'Τι μάρκα αμάξι έχεις;'
        ans1 = 'Citroen'
        ans2 = 'Toyota'
        ans3 = 'Skoda'
        ans4 = 'Fiat'
    return question, ans1, ans2, ans3, ans4

    
def correct_answers():
    ans = {1:3, 2:1, 3:2, 4:4, 5:2, 6:3, 7:4, 8:3, 9:1, 10:2}
    return ans

def play_game(questions_objs):
    p1_corr_score = 0
    p2_corr_score = 0
    answers = correct_answers()
    
    print('\n--- Παιχνίδι Ερωτήσεων ---')
    print()

    for i in range(1, 11):
        row = i
        question, ans1, ans2, ans3, ans4 = questions_objs(row)
        ans = answers[i]
        if i % 2 == 0:
            print('\n-- Σειρά του Παίκτη 1 --')
            ques = Question(question, ans1, ans2, ans3, ans4, ans)
            ques.ask_question()
            choice = int(input('\nΔώσε την απάντησή σου(1-4): '))
            if choice == ques.get_corr_ans():
                p1_corr_score += 1
        else:
            print('\n-- Σειρά του Παίκτη 2 --')
            ques = Question(question, ans1, ans2, ans3, ans4, ans)
            ques.ask_question()
            choice = int(input('\nΔώσε την απάντησή σου(1-4): '))
            if choice == ques.get_corr_ans():
                p2_corr_score += 1
    
    print(f'\nΣκορ Παίχτη 1: {p1_corr_score}')
    print(f'\nΣκορ Παίχτη 2: {p2_corr_score}')
    print()
    if p1_corr_score > p2_corr_score:
        print('ΚΕΡΔΙΣΕ Ο ΠΑΙΧΤΗΣ 1 !!!')
        print()
    elif p1_corr_score < p2_corr_score:
        print('ΚΕΡΔΙΣΕ Ο ΠΑΙΧΤΗΣ 2 !!!')
        print()
    else:
        print('ΕΙΝΑΙ ΙΣΟΠΑΛΛΙΑ !!!')
        print()


def main():
    play_game(questions_objs)
main()