# Test program using accounts
# Version 1, usando variables explicitas para cada objeto cuenta

# Esta linea importa todo del archivo Account.py
from Account import *
# Se crean dos cuentas
oJoesAccount = Account('Joe', 100, 'JoesPassword')
print("Created an account for Joe")
oMarysAccount = Account('Mary', 12345, 'MarysPassword')
print("Created an account for Mary")

oJoesAccount.show()
oMarysAccount.show()
print()
# Llamado a los metodos de cada cuenta segun su transaccion
print('Calling methods of the two accounts ...')
oJoesAccount.deposit(50, 'JoesPassword')
oMarysAccount.withdraw(345, 'MarysPassword')
oMarysAccount.deposit(100, 'MarysPassword')
# Muestra las cuentas
oJoesAccount.show()
oMarysAccount.show()

# ================================================

# Creacion de una cuenta solicitando info por input
print("**********************************************************")

userName = input('What is the name for the new user account? ') 
userBalance = input('What is the starting balance for this account? ')
userBalance = int(userBalance)
userPassword = input('What is the password you want to use for this account? ')

#se crea la nueva cuenta con los datos suministrados
oNewAccount = Account(userName, userBalance, userPassword) 


# Se muestra en consola la nueva cuenta creada
oNewAccount.show() 
# Se depositan $100
oNewAccount.deposit(100, userPassword) 
usersBalance = oNewAccount.getBalance(userPassword)
print()
print('After depositing 100, the user\'s balance is:', usersBalance)
# Se muestra el estado actual de la cuenta
oNewAccount.show()