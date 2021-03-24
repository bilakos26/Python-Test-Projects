import BankAccount

def main():
    start_bal = float(input('Give your initial balance: '))

    savings = BankAccount.BankAccount(start_bal)

    #The first job payment to the user
    pay = float(input('How much money did you get paid from work this week?: '))
    print("I'm gonna deposit this amount of money, on your Bank Account.")
    savings.deposit(pay)

    #Display the current balance
    print('Your Bank Account Balance is: %.2f€'%(savings.getbalance()))

    #Entry of the withdrawal amount
    cash = float(input('How much money do you want to withdraw, from your Bank Account?: '))
    print("I'm gonna remove this amoun of money, from your Bank Account.")
    savings.withdraw(cash)

    #Display the current balance
    print(savings)


main()