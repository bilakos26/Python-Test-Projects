class BankAccount:

    def __init__(self, bal):
        self.__balance = bal

    
    def deposit(self, amount):
        self.__balance += amount


    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print('Error. Not enough money in the bank account.')
    

    def getbalance(self):
        return self.__balance

    
    def __str__(self):
        return 'Your Bank Account Balance is: %.2f€'%(self.__balance)