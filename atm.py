class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
    def __str__(self):
        return f' Mr {self.name} your current balance is {self.balance}'
    
    def deposit(self,amount):
        self.balance += amount
        return f' Deposit successful and your balalce is {self.balance}'
    def withdraw(self, amount):
        if amount > self.balance:
            return f'insufficient funds'
        else:
            self.balance -= amount
            return f'Withdrawl Successful. Your Balalce is {self.balance}'
        
        


print('Welcome to Zenith Bank!')
info =input('Please Enter Your Name \n')
user=Account(info)


while True:
    choice = input("""
        what will you like to do?
        press b to check your balance
        press d to deposite
        press w to withdraw                       
            """)
    if choice.upper() == 'B':
        print(user)
    elif choice.upper() == 'D':
        amount= int(input("Enter Amount     \n"))
        if amount <=0:
            print('Invalid Transaction')
        else:
            print(user.deposit(amount))
    elif choice.upper() == 'W':
        amount= int(input("Enter Transaction Amount \n"))
        if amount <= 0:
            print('Invalid Transaction Amount')
        else:
            print(user.withdraw(amount))
    question = input('Do you want to perform another transaction? \n (y/n): ')
    if question.lower() == 'y':
        continue
    else:
        print('Thank you Have a nice day')
        break


