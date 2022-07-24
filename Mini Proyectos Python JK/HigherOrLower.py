# Taller 4 
# SENA estructuras de datos en python 2022
# Juan Carlos Bohorquez
import random

# card constants
SUIT_TUPLE = ('Picas', 'Corazones', 'Treboles', 'Diamantes')
RANK_TUPLE = ('As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')
N_CARDS = 8


def getCard(deckListIn):
    thisCard = deckListIn.pop() 
    return thisCard


def shuffle(deckListIn):
    deckListOut = deckListIn.copy() 
    random.shuffle(deckListOut)
    return deckListOut
    
# Main code
print('****************************************************************')
print('   Bienvenido a Adivina si la carta es mayor o menor.')
print('****************************************************************')
print('Debes escoger si la siguiente carta es mayor \no es menor que la carta actual.')
print('****************************************************************')
print('Si aciertas te llevas 20 puntos; si fallas pierdes 15 puntos.')
print('Tienes 50 puntos para empezar. \n')
print('****************************************************************')

startingDeckList = []

for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank': rank, 'suit': suit, 'value': thisValue +1}
        startingDeckList.append(cardDict)
score = 50

while True: # play multiple games
    print()
    gameDeckList = shuffle(startingDeckList)
    currentCardDict = getCard(gameDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']
    print('La carta inicial es: ', currentCardRank + ' de ' + currentCardSuit)
    print()

    for cardNumber in range(0, N_CARDS):
        answer = input('Sera la siguiente carta mayor o menor que el ' + currentCardRank + ' de ' + currentCardSuit + '? (responde h para mayor o l para menor):')
        answer = answer.casefold() # force lowercase

        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']
        print('La siguiente carta es: ', nextCardRank + ' de ' + nextCardSuit)

        if answer == 'h':
            if nextCardValue > currentCardValue:
                print('Correcto!! , la carta era mayor!!!.')
                score = score + 20
            else:
                print('Lo siento, la carta era mayor')
                score = score -15
        elif answer == 'l':
            if nextCardValue < currentCardValue:
                score = score + 20
                print('Correcto!!!, la carta era menor!!!')
            else:
                score = score -15
                print('Lo siento, la carta era menor')

        print('Tu puntaje es: ', score)
        print()
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue
    goAgain = input('Para jugar de nuevo, presiona ENTER, o "q" para salir del juego: ')
    if goAgain == 'q':
        break
    print('OK Adios!!!')