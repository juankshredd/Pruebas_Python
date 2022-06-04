# Non-OOP
# Bank 2
# Single account

accountName = ''
accountBalance = 0
accountPassword = ''

def newAccount(name, balance, password):
    global accountName, accountBalance, accountPassword
    accountName = name
    accountBalance = balance
    accountPassword = password

def show():
    global accountName, accountBalance, accountPassword
    print('         name: ', accountName)
    print('         balance: ', accountBalance)
    print('         password: ', accountPassword)
    print('********************************************')

def getBalance(password):
    global accountName, accountBalance, accountPassword
    if password != accountPassword:
        print('Incorrect Password')
        return None
    return accountBalance

def deposit(depositAmount, password):
    global accountName, accountBalance, accountPassword
    if depositAmount < 0:
        print('You cannot deposit a negative amount.')
        return None
    if password != accountPassword:
        print('Incorrect Password.')
        return None
    accountBalance = accountBalance + depositAmount
    return accountBalance

def withdrawal(withdrawalAmount, password):
    global accountName, accountBalance, accountPassword
    if withdrawalAmount < 0:
        print('You cannot withdraw a negative amount.')
        return None
    elif withdrawalAmount > accountBalance:
        print('Your balance is not enough.')
        return None
    elif password != accountPassword:
        print('Incorrect password.')
        return None
    accountBalance = accountBalance - withdrawalAmount
    return accountBalance

newAccount('Juan', 100, 'pass') # this call creates a new account with these parameters

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
        if userPassword != accountPassword:
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
        newBalence = withdrawal(userWithdrawalAmount, userPassword)
        if newBalance is not None:
            print('Your new balance is: ', newBalance)
    elif action == 's':
        userPassword = input('Enter your password: ')
        if userPassword != accountPassword:
            print('Incorrect password.')
        show()
    elif action == 'q':
        break
    print('Done.')