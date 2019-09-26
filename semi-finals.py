class Account:
    def __init__(self):
        self.fname = ''
        self.lname = ''
        self.fullname = ''
        self.cashDeposit = ''
        self.cashWithdrawal = ''
        self.remainingBalance = ''

    def setFname(self, fname):
        self.fname = fname

    def setLname(self, lname):
        self.lname = lname

    def getFullname(self):
        self.fullname = self.fname + ' ' + self.lname

    def deposit(self, cashDeposit):
        self.remainingBalance = (self.remainingBalance + cashDeposit)
        return self.remainingBalance

    def withdraw(self, cashWithdrawal):
        result = self.remainingBalance - cashWithdrawal
        if result >= 0:
            self.remainingBalance = (self.remainingBalance - cashWithdrawal)
        else:
            print('ERROR: Withdrawal amount is more than remaining balance')
            exit()

    def getRemainingBalance(self):
        return self.remainingBalance


first_name = input("Please enter First Name of the first account: ")
last_name = input("Please enter Last Name of the first account: ")
initial_balance = int(input("Please enter initial balance First Name of the first account: "))
person = Account()
person.fname = first_name
person.lname = last_name
person.remainingBalance = initial_balance

first_name1 = input("Please enter  First Name of the second account: ")
last_name1 = input("Please enter Last Name of the second account: ")
initial_balance1 = int(input("Please enter initial balance First Name of the second account: "))
person1 = Account()
person1.fname = first_name
person1.lname = last_name
person1.remainingBalance = initial_balance

loop = 'true'
while loop == 'true':
    print("1. Check Balance")
    print("2. Deposit Cash")
    print("3. Withdraw Cash")
    print("4. EXIT")
    var = int(input("SELECT OPTION: "))
    if var == 1:
        person.getFullname()
        firstName = input("Please enter the fname of the account: ")
        if firstName == person.fname:
            print('Account: {} remaining balance is {}'.format(person.fullname, person.remainingBalance))
        else:
            print('Account: {} remaining balance is {}'.format(person1.fullname, person1.remainingBalance))
    elif var == 2:
        firstName = input("Please enter the fname of the account: ")
        if firstName == person.fname:
            amount = int(input("Please enter the amount to be deposited: "))
            person.deposit(amount)
            print('{} Your updated remaining balance is {}'.format(person.fullname, person.remainingBalance))
        else:
            amount = int(input("Please enter the amount to be deposited: "))
            person1.deposit(amount)
            print('{} Your updated remaining balance is {}'.format(person1.fullname, person1.remainingBalance))

    elif var == 3:
        if firstName == person.fname:
            amount = int(input("Please enter the amount to be withdrawn: "))
            person.withdraw(amount)
            print('{} Your updated remaining balance is {}'.format(person.fullname, person.remainingBalance))
        else:
            amount = int(input("Please enter the amount to be withdrawn: "))
            person1.withdraw(amount)
            print('{} Your updated remaining balance is {}'.format(person1.fullname, person1.remainingBalance))

    elif var == 4:
        exit()
        break
