# Non-OOP Bank
# Version 5
# Any number of accounts - with a list of dictionaries

accountList = []

def newAccount(aName, aBalance, aPassword):
    global accountList
    newAccountDict = {
        'name': aName,
        'balance': aBalance,
        'password': aPassword
    }
    accountList.append(newAccountDict)

def show(accountNumber, password):
    global accountList
    print('Account', accountNumber)
    thisAccountDict = accountList[accountNumber]
    if password != thisAccountDict['password']:
        print('Incorrect password.\n')
        return None
    print('======================================')
    print(' Name', thisAccountDict['name'])
    print(' Balance:', thisAccountDict['balance'])
    print(' Password:', thisAccountDict['password'])
    print('======================================')

def getBalance(accountNumber, password):
    global accountList
    thisAccountDict = accountList[accountNumber]
    if password != thisAccountDict['password']:
        print('Incorrect password.\n')
        return None
    return thisAccountDict['balance']

#--- snipped additional deposit() and withdraw() functions ---
# Create two sample accounts

def deposit(accountNumber, password, deposit):
    global accountList
    thisAccountDict = accountList[accountNumber]
    if password != thisAccountDict['password']:
        print('Incorrect password.\n')
        return None
    if deposit < 0:
        print('You cannot deposit negative amounts.\n')
        return None
    thisAccountDict['balance'] = thisAccountDict['balance'] + deposit
    return thisAccountDict['balance']

def withdraw(accountNumber, password, withdraw):
    global accountList
    thisAccountDict = accountList[accountNumber]
    if password != thisAccountDict['password']:
        print('Incorrect password.\n')
    if withdraw < 0:
        print('You cannot withdraw a negative amount.\n')
        return None
    elif withdraw > thisAccountDict['balance']:
        print('Your balance do not allow this operation.\n')
        return None
    thisAccountDict['balance'] = thisAccountDict['balance'] - withdraw
    return thisAccountDict['balance']


print('Joe\'s account is account number: ', len(accountList))
newAccount('Joe', 100, 'soup')

print('Mary\'s account is account number: ', len(accountList))
newAccount('Mary',12345, 'nuts')

while True:
    print('======================================')
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press n to create a new account')
    print('Press w to make a withdrawal')
    print('Press s to show all accounts')
    print('Press q to quit')
    print('======================================')

    action = input('What do you want to do?: \n').lower()
    action = action[0]
    print('======================================')

    if action == 'b':
        print('Get Balance: \n')
        userAccountNumber = int(input('Please enter your account number : \n'))
        userPassword = input('Please enter the password: \n')
        theBalance = getBalance(userAccountNumber, userPassword)
        if theBalance != None:
            print('Your balance is: ', theBalance)
    elif action == 'd':
        print('Make a deposit: \n')
        userAccountNumber = int(input('Please enter your account number : \n'))
        userPassword = input('Please enter the password: \n')
        userDepositAmount = int(input('Enter the deposit amount: \n'))
        newBalance = deposit(userAccountNumber, userPassword, userDepositAmount)
        if newBalance != None:
            print('Your new balance is: \n', newBalance)
    elif action == 'n':
        print('Create new account: \n')
        userName = input('Please enter your name: \n')
        userInitialBalance = int(input('Please enter your initial balance: \n'))
        initialPassword = input('Setup your password: \n')
        userAccountNumber = len(accountList)
        initalInfo = newAccount(userName, userInitialBalance, initialPassword)
        print('Your new account number is: ', userAccountNumber)
# --- snipped additional user interface ---
    elif action == 's':
        print('Show Account data: \n')
        userAccountNumber = int(input('Enter your account number: \n'))
        userPassword = input('Enter your password: \n')
        info = show(userAccountNumber, userPassword)

    elif action == 'w':
        print('Make a withdraw: \n')
        userAccountNumber = int(input('Please enter your account number : \n'))
        userPassword = input('Please enter the password: \n')
        withdrawAmount = int(input('Enter the withdraw amount: \n'))
        newBalance = withdraw(userAccountNumber, userPassword, withdrawAmount)
        if newBalance != None:
            print('Your new balance is: ', newBalance)

    elif action == 'q':
        break
    print('Done')