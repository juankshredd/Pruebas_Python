print('Bienvenido a JK ATM')
restart=('Y')
chances=3
balance=999.25

while chances >= 0:
    pin=int(input('Ingrese su pin:  '))
    if pin==(0000):
        print('Pin Correcto')
        print('Presione 1 para Saldo')
        print('Presione 2 para Retiro en Efectivo')
        print('Presione 3 para Pagos')
        print('Presione 4 para Retornar Tarjeta')
        
        while restart not in ('n', 'N', 'no', 'NO', 'No', 'nO'):
            print('Presione 1 para Saldo')
            print('Presione 2 para Retiro')
            print('Presione 3 para Pagos')
            print('Presione 4 para Retornar Tarjeta')
            option= int(input('Que desea elegir? '))
            if option==1:
                print('Su saldo es: $ ', balance)
                restart=input('Desea regresar?')
                if restart in ('n', 'no', 'N', 'NO', 'nO', 'No'):
                    print('Gracias')
                    break
            elif option==2:
                option2= ('Y')
                withdrawl= float(input('Cuanto desea retirar? 10, 20, 40, 60, 80  para otra cifra oprima 1: '))
                if withdrawl in [10, 20, 40, 60, 80]:
                    balance=balance-withdrawl
                    print('Ahora tu saldo es: ',balance)
                    restart=input('Desea regresar? ')
                    if restart in ('n', 'N', 'no', 'NO', 'nO', 'No'):
                        print('Gracias')
                        break
                    elif withdrawl != [10, 20, 40, 60, 80]:
                        print('Cantidad invalida, por favor intente otra vez')
                        restart= ('Y')
                    elif withdrawl==1:
                        withdrawl=float(input('Ingrese Cantidad: '))
            elif option==3:
                pay_in=float(input('Cantidad a pagar'))        
                balance= balance + pay_in
                print('Su nuevo saldo es: ', balance)     
                restart=input('Desea Regresar? ')  
                if restart in ('n', 'N', 'no', 'NO', 'nO', 'No'):
                    print('Gracias')    
                    break          
            elif option==4:
                print('Espere un momento...puede tomar su tarjeta')
                print('Gracias')
                break
            else:
                print('Elija una opcion valida!')
                restart=('Y')
    elif pin != (0000):
        print('Clave Incorrecta!')
        chances=chances -1
        if chances==0:
            print('No hay mas intentos!')
            break
        