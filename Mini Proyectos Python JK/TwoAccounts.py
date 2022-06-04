# non OOP
# Bank 3
# Two accounts Even with just two accounts, you can see that this approach gets out of hand quickly.
# this code has several errors because of it's poor good practice uses

account0Name = ''
account0Balance = ''
account0Password = ''
account1Name = ''
account1Balance = ''
account1Password = ''
nAccounts = 0

def newAccount(accountNumber, name, balance, password):
    global account0Name, account0Balance, account0Password # This is a bad practice. 
    global account1Name, account1Balance, account1Password # Methods should not to modify global variables

    if accountNumber == 0:
        account0Name = name
        account0Balance = balance
        account0Password = password
    if accountNumber == 1:
        account1Name = name
        account1Balance = balance
        account1Password = password

def show():
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if account0Name != '':
        print('Account 0')
        print(' Name', account0Name)
        print(' Balance:', account0Balance)
        print(' Password:', account0Password)
        print()
    if account1Name != '':
        print('Account 1')
        print(' Name', account1Name)
        print(' Balance:', account1Balance)
        print(' Password:', account1Password)
        print()

def getBalance(accountNumber, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if accountNumber == 0:
        if password != account0Password:
            print('Incorrect password')
            return None
        return account0Balance
    if accountNumber == 1:
        if password != account1Password:
            print('Incorrect password')
            return None
        return account1Balance

def deposit(accountNumber, depositAmount, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if accountNumber == 0:
        if password != account0Password:
            print('Incorrect password')
            return None
        if depositAmount < 0:
            print('You cannot deposit negative amounts')
            return None
        if depositAmount > account1Balance:
            print('Amount exceed your balance')
            return None
        account0Balance = account0Balance + depositAmount
        return account0Balance
    if accountNumber == 1:
        if password != account1Password:
            print('Incorrect password')
            return None
        if depositAmount < 0:
            print('You cannot deposit negative amounts')
            return None
        if depositAmount > account1Balance:
            print('Amount exceed your balance')
            return None
        account1Balance = account1Balance + depositAmount
        return account1Balance

def withdraw(accountNumber, password, withdrawAmount):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if accountNumber == 0:
        if password != account0Password:
            print('Incorrect password')
            return None
        if withdrawAmount < 0:
            print('You cannot withdraw negative amounts')
            return None
        account0Balance = account0Balance - withdrawAmount
        return account0Balance

    if accountNumber == 1:
        if withdrawAmount < 0:
            print('You cannot withdraw negative amounts')
            return None
        if withdrawAmount > account1Balance:
            print('Amount exceed your balance')
            return None
        account1Balance = account1Balance - withdrawAmount
        return account1Balance

newAccount(0, 'Juan', 100, 'abcd') # this call creates a new account with these parameters
newAccount(1, 'Luisa', 400, 'tern')
while True:
    print('*************************************')
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawal')
    print('Press s to show the account')
    print('Press q to quit')
    print('*************************************')

    action = input('What do you want to do?: ').lower()
    action = action[0]
    print('*************************************')

    
    if action == 'b':
        print('Get balance: ')
        userPassword = input('Enter your password: ')
        if userPassword != account0Password:
            theBalance = getBalance(userPassword)
            if theBalance is not None:
                print('Your balence is: ', theBalance)
    elif action == 'd':
        print('Deposit: ')
        userDepositAmount = input('Enter the amount to deposit: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Enter your password: ')
        newBalance = deposit(userDepositAmount, userPassword)
        if newBalance is not None:
            print('Your new balance is: ', newBalance)
    elif action == 'w':
        print('Withdrawal')
        userWithdrawalAmount = int(input('Enter the amount to withdraw'))
        userPassword = input('Enter your password: ')
        newBalence = withdraw(userWithdrawalAmount, userPassword)
        if newBalance is not None:
            print('Your new balance is: ', newBalance)
    elif action == 's':
        userPassword = input('Enter your password: ')
        if userPassword != account0Password:
            print('Incorrect password.')
        if userPassword != account1Password:
            print('Incorrect password')
        show()
        

    elif action == 'q':
        break
    print('Done.')