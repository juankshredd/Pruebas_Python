# Non-OOP Bank
# Version 4
# Any number of accounts - with lists


accountNamesList = []
accountBalancesList = []
accountPasswordsList = []

def newAccount(name, balance, password):
    global accountNamesList, accountBalancesList, accountPasswordsList
    accountNamesList.append(name)
    accountBalancesList.append(balance)
    accountPasswordsList.append(password)

def show(accountNumber):
    global accountNamesList, accountBalancesList, accountPasswordsList
    print('Account', accountNumber)
    print('        Name', accountNamesList[accountNumber])
    print('        Balance', accountBalancesList[accountNumber])
    print('        Password', accountPasswordsList[accountNumber])

def getBalance(accountNumber, password):
    global accountNamesList, accountBalancesList, accountPasswordsList
    if password != accountPasswordsList[accountNumber]:
        print('Incorrect password')
        return None
    return accountBalancesList[accountNumber]

#--- snipped additional functions ---
# Create two sample accounts

def deposit(accountNumber, password, depositAmount):
    global accountNamesList, accountBalancesList, accountPasswordsList
    if password != accountPasswordsList[accountNumber]:
        print('Incorrect password')
        return None
    elif depositAmount < 0:
        print('You cannot deposit negative amounts')
        return None
    else:
        accountBalancesList[accountNumber] = accountBalancesList[accountNumber] + depositAmount
        print('Your current balance is: ', accountBalancesList[accountNumber])
        return accountBalancesList[accountNumber]

def withdraw(accountNumber, password, withdrawAmount):
    global accountNamesList, accountBalancesList, accountPasswordsList
    if password != accountPasswordsList[accountNumber]:
        print('Incorrect password')
        return None
    elif withdrawAmount < 0:
        print('You cannot withdraw negative amounts')
        return None
    elif withdrawAmount > accountBalancesList[accountNumber]:
        print('Your balance is not enough')
        return None
    else:
        accountBalancesList[accountNumber] = accountBalancesList[accountNumber] - withdrawAmount
        print('Your current balance is: ', accountBalancesList[accountNumber])


# print('Jose\'s  account is account number: ', len(accountNamesList))
# newAccount('Jose', 1000, 'west')
# print('Lilia\'s account is account number: ', len(accountNamesList))
# newAccount('Lilia', 5000, 'port')

while True:
    print('|===============================|')
    print('| WELCOME TO JABALI\'S BANK      |')
    print('|===============================|')
    print('|Press b to get the balance     |')
    print('|Press d to make a deposit      |')
    print('|Press n to create a new account|')
    print('|Press w to make a withdrawal   |')
    print('|Press s to show all accounts   |')
    print('|Press q to quit                |')
    print('|===============================|')

    action = input('What do you want to do? \n')
    action = action.lower()
    action = action[0]
    print('|===============================|')

    if action == 'b':
        print('Get Balance: ')
        userAccountNumber = int(input('Please enter your account number.\n'))
        userPassword = input('Please enter your password\n')
        theBalance = getBalance(userAccountNumber, userPassword)
        if theBalance != None:
            print('Your balance is: ', theBalance)
    #--- snipped additional user interface ---
    elif action == 'd':
        print('Make a Deposit: ')
        userAccountNumber = int(input('Please enter your account number.\n'))
        userPassword = input('Please enter your password\n')
        userDepositAmount = int(input('Enter the withdraw amount\n'))
        theBalance = deposit(userAccountNumber, userPassword, userDepositAmount)
    
    elif action == 's':
        print('Show Account: ')
        userAccountNumber = int(input('Please enter your account number.\n'))
        info = show(userAccountNumber)

    elif action == 'n':
        print('Create a new account: \nPlease enter info:\n')
        userName = input('Enter client\'s name: \n')
        userInitBalance = int(input('Enter the initial balance amount: \n'))
        userFirstPassword = input('Enter the first password ever for this account\n')
        info = newAccount(userName, userInitBalance, userFirstPassword)

    elif action == 'w':
        print('Make a withdraw: \n')
        userAccountNumber = int(input('Please enter your account number.\n'))
        userPassword = input('Please enter your password\n')
        userWithdrawAmount = int(input('Enter the withdraw amount: \n'))
        theBalance = withdraw(userAccountNumber, userPassword, userWithdrawAmount)

    elif action == 'q':
        break

    print('Done')   