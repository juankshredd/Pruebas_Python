# Test program using accounts
# Version 2, using a list of accounts
# Bring in all the code from the Account class file
from Account import *
# Start off with an empty list of accounts
accountsList = [ ] 
# Crea 2 cuentas
oAccount = Account('Joe', 100, 'JoesPassword') 
accountsList.append(oAccount)
print("Joe's account number is 0")
oAccount = Account('Mary', 12345, 'MarysPassword') 
accountsList.append(oAccount)
print("Mary's account number is 1")
accountsList[0].show() 
accountsList[1].show()
print()
# Se llaman algunos metodos
print('Calling methods of the two accounts ...')
accountsList[0].deposit(50, 'JoesPassword') 
accountsList[1].withdraw(345, 'MarysPassword') 

accountsList[1].deposit(100, 'MarysPassword') 
# Muestra 2 cuentas
accountsList[0].show() 
accountsList[1].show()
# Crea una cuenta solicitando info al usuario
print()
userName = input('What is the name for the new user account? ')
userBalance = input('What is the starting balance for this account? ')
userBalance = int(userBalance)
userPassword = input('What is the password you want to use for this account? ')
oAccount = Account(userName, userBalance, userPassword)
accountsList.append(oAccount) # ingresa la nueva cuenta a la lista de cuentas
# Muestra la nueva cuenta creada
print('Created new account, account number is 2')
accountsList[2].show()
# Se hace un deposito de $100
accountsList[2].deposit(100, userPassword)
usersBalance = accountsList[2].getBalance(userPassword)
print()
print('After depositing 100, the user\'s balance is:', usersBalance)
# Muestra la nueva cuenta
accountsList[2].show()

# Esto imprime la direccion en memoria de la lista de cuentas
print(accountsList)