"""Bagels, by JK
A deductive logic game where you must guess a number based on clues. 2022"""
import random

from numpy import number
NUM_DIGITS = 100
MAX_GUESSES = 1000

def main():
    print('''Bagels, a dedcutive logic game.
    By JK  
    
    Estoy pensando en un numero de {} digitos, ninguno se repite
    Trata de adivinar cual numero es. He aquí unas pistas:
    Cuando diga:     Esto significa:
    Pico             Un digito es correcto, pero en una posicion equivocada.
    Fermi            Cuando un digito es correcto y esta en la posicion correcta:
    Bagels           Ningun digito es correcto.
    
    Por ejemplo, si el numero secreto fuera 248 y tu intento fue 843 las pistas serian Fermi Pico'''.format(NUM_DIGITS))

    while True:
        secretNum = getSecretNum()
        print('He pensado un numero')
        print('Tienes {} intentos para adivinar'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''

            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses +=1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print('Te quedaste sin Mas Intentos...')
                print('El numero secretio era: {}.'.format(secretNum))
        print('Quieres jugar de nuevo? (si o no)')
        if input('> ').lower().startswith('s'):
            break
    print('Gracias por jugar.')

def getSecretNum():
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(number[i])
    return secretNum

def getClues(guess, secretNum):
    if guess == secretNum:
        return ' Lo lograste!!'
    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ''.join(clues)

if __name__=='__main__':
    main()