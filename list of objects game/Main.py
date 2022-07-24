from Monster import *
N_MONSTERS = 20
N_ROWS = 100 # could be any size
N_COLS = 200 # could be any size
MAX_SPEED = 4
monsterList = [] # start with an empty list
for i in range(N_MONSTERS):
    oMonster = Monster(N_ROWS, N_COLS, MAX_SPEED) # create a Monster
    monsterList.append(oMonster) # add the Monster to our list
for oMonster in monsterList:
    oMonster.move()