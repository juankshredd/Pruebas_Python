# Account class *** PRIMER ACERCAMIENTO A CLASES-- ESTE CODIGO NO CORRE****

class Account():
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = int(balance)
        self.password = password
    
    def deposit(self, amountTodeposit, password):
        if password != self.password:
            print('Sorry, incorrect password.\n')
            return None
        if amountTodeposit < 0:
            print('Sorry, you cannot deposit a negative amount.\n')
            return None
        self.balance = self.balance + amountTodeposit
        return self.balance

    def withdraw(self, amountToWithdraw, password):
        if password != self.password:
            print('Sorry, incorrect password.\n')
            return None
        if amountToWithdraw < 0:
            print('Sorry, you cannot withdraw a negative amount.\n')
            return None
        elif amountToWithdraw > self.balance:
            print('Sorry, you cannot withdraw more than your balance.\n')
            return None
        self.balance = self.balance - amountToWithdraw
        return self.balance

    # Added for debugging

    def show(self):
        print('===============================')
        print('        Account data           ')
        print(' Name:', self.name)
        print(' Balance:', self.balance)
        print(' Password:', self.password)
        print('===============================')

    # Falta crear el resto del codigo