class User():
    def __init__(self, owner, age, date_of_birth):
        self.owner = owner
        self.age = age
        self.date_of_birth = date_of_birth

    def account_summary(self):
        print(f"\nPersonal Information\nName: {self.owner}\nAge: {self.age}\nDOB: {self.date_of_birth} ")
        
class CheckingAccount(User):
    def __init__(self, owner, age, date_of_birth):
        super().__init__(owner, age, date_of_birth)
        self.balance = 0

    def summary(self):
        self.account_summary()
        print(f'Account Balance: ${self.balance:.2f}')

    def deposit (self,dep_amount):
        self.dep_amount = dep_amount
        self.balance += dep_amount
        print(f'You have successfully deposited ${self.dep_amount:.2f}')
        print(f'Your new account balance is: ${self.balance:.2f}')

    def withdraw (self,withdraw_amount):
        self.withdraw_amount = withdraw_amount
        if self.balance >= withdraw_amount:
            self.balance -= withdraw_amount
            print(f'You have successfully withdrew ${self.withdraw_amount:.2f}')
            print(f'Your new account balance is: ${self.balance:.2f}')
        else:
            print(f'You have insufficent funds. Please try again.\nBalance avaliable: ${self.balance:.2f}')

class SavingsAccount(User):
    def __init__(self, owner, age, date_of_birth):
        super().__init__(owner, age, date_of_birth)
        self.balance = 0

    def summary(self):
        self.account_summary()
        print(f'Account Balance: ${self.balance:.2f}')

    def deposit (self,dep_amount):
        self.dep_amount = dep_amount
        self.balance += dep_amount
        print(f'You have successfully deposited ${self.dep_amount:.2f}')
        print(f'Your new account balance is: ${self.balance:.2f}')

    def withdraw (self,withdraw_amount):
        self.withdraw_amount = withdraw_amount
        if self.balance >= withdraw_amount:
            self.balance -= withdraw_amount
            print(f'You have successfully withdrew ${self.withdraw_amount:.2f}')
            print(f'Your new account balance is: ${self.balance:.2f}')
        else:
            print(f'You have insufficent funds. Please try again.\nBalance avaliable: ${self.balance:.2f}')

class BusinessAccount(User):
    def __init__(self, owner, age, date_of_birth):
        super().__init__(owner, age, date_of_birth)
        self.balance = 0

    def summary(self):
        self.account_summary()
        print(f'Account Balance: ${self.balance:.2f}')

    def deposit (self,dep_amount):
        self.dep_amount = dep_amount
        self.balance += dep_amount
        print(f'You have successfully deposited ${self.dep_amount:.2f}')
        print(f'Your new account balance is: ${self.balance:.2f}')

    def withdraw (self,withdraw_amount):
        self.withdraw_amount = withdraw_amount
        if self.balance >= withdraw_amount:
            self.balance -= withdraw_amount
            print(f'You have successfully withdrew ${self.withdraw_amount:.2f}')
            print(f'Your new account balance is: ${self.balance:.2f}')
        else:
            print(f'You have insufficent funds. Please try again.\nBalance avaliable: ${self.balance:.2f}')


print('Welcome to the Bissu ATM!')
name = input('Please enter your name: ')
age = int(input('Please enter your age: '))
date_of_birth = input('What is your date of birth?: ')
Checking = CheckingAccount(name,age,date_of_birth)
Savings = SavingsAccount(name,age,date_of_birth)
Business = BusinessAccount(name,age,date_of_birth)

inAccountSelection = True

while inAccountSelection:
    account_type = input(f"Hello there {name}. Which account would you like to access today?\nType 'c' for checking account\nType 's' for savings account\nType 'b' for business account\nType 'q' to quit the ATM system\n: ").lower()
    
    if account_type == 'c':
        session = True
        while session:
            action = input("\nType 'd' to deposit money\nType 'w' to withdraw money\nType 'summary' to view a summary of your account\nType 'm' to go to main menu\n: ").lower()
            if action == 'd':
                dep_amount = float(input('How much would you like to deposit?: '))
                Checking.deposit(dep_amount)
            elif action == 'w':
                with_amount = float(input('How much would you like to withdraw? '))
                Checking.withdraw(with_amount)
            elif action == 'summary':
                Checking.summary()
            elif action == 'm':
                session = False
            else:
                print('Invalid input. Please try again.')

    elif account_type == 's':
        session = True
        while session:
            action = input("\nType 'd' to deposit money\nType 'w' to withdraw money\nType 'summary' to view a summary of your account\nType 'm' to go to main menu\n: ").lower()
            if action == 'd':
                dep_amount = float(input('How much would you like to deposit?: '))
                Savings.deposit(dep_amount)
            elif action == 'w':
                with_amount = float(input('How much would you like to withdraw? '))
                Savings.withdraw(with_amount)
            elif action == 'summary':
                Savings.summary()
            elif action == 'm':
                session = False
            else:
                print('Invalid input. Please try again.')

    elif account_type == 'b':
        session = True
        while session:
            action = input("\nType 'd' to deposit money\nType 'w' to withdraw money\nType 'summary' to view a summary of your account\nType 'm' to go to main menu\n: ").lower()
            if action == 'd':
                dep_amount = float(input('How much would you like to deposit?: '))
                Business.deposit(dep_amount)
            elif action == 'w':
                with_amount = float(input('How much would you like to withdraw? '))
                Business.withdraw(with_amount)
            elif action == 'summary':
                Business.summary()
            elif action == 'm':
                session = False
            else:
                print('Invalid input. Please try again.')
    
    elif account_type == 'q':
        inAccountSelection = False 
    
    else:
        print('That is an invalid command. Please try again.')

print('Thank you for using the Bissu ATM!')
print('Shutting down....')
