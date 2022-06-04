# Bank Account NO OOP
accountName = 'joe'
accountBalance = 100
accountPassword = '1234'

while True:
    print('******************************')
    print('     WELCOME TO ATM V2.0      ')
    print('******************************')
    print('press b to get the balance: ')
    print('press d to make a deposit: ')
    print('press w to make a withdrawl: ')
    print('press s to show account: ')
    print('press q to quit: ')
    print('******************************')

    action = input('What do you want to do?: ')
    action = action.lower() # force to lowercase
    action = action[0] # using just the first letter
    print('******************************')

    if action == 'b':
        print('get balance: ')
        userPassword = input('Enter your password: ')
        if userPassword != accountPassword:
            print('Incorrect Password.')
        else:
            print('Your balance is: ', accountBalance)
    elif action == 'd':
        print('Deposit: ')
        userPassword = input('Enter your password')
        if userPassword != accountPassword:
            print('Incorrect Password.')
        else:
            userDepositAmount = int(input('Enter the amount to deposit: '))
            if userDepositAmount < 0:
                print('You cannot deposit a negative amount.')
            elif userPassword != accountPassword:
                print('Incorrect Password.')
            else: # all is OK
                accountBalance = accountBalance + userDepositAmount
                print('Your new balance is: ', accountBalance)
    elif action == 's':
        print('Show account: ')
        userPassword = input('Enter your password')
        if userPassword != accountPassword:
            print('Incorrect Password.')
        else:
            print('      USER PROFILE:      ')
            print('******************************')
            print('      name: ', accountName)
            print('      balance: ', accountBalance)
            print('      account password: ', accountPassword)
            print('******************************')
    elif action == 'q':
        break
    elif action == 'w':
        print('Make a withdrawal: ')
        userPassword = input('Enter your password')
        if userPassword != accountPassword:
            print('Incorrect Password.')
        else:
            print('Enter the withdrawal amount: ')
            userWithdrawalAmount = int(input('Enter the amount to withdrawal: '))
            if userDepositAmount < 0:
                print('You cannot withdraw a negative amount.')
            elif userWithdrawalAmount > accountBalance:
                print('The amount exceed your balance.')
            else:
                accountBalance = accountBalance - userWithdrawalAmount
                print('Your new balance is: ', accountBalance)
    print('done.')