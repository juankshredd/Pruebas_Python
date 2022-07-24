from Player import *

players = []
        
player1 = Player()
players.append(player1)
player1.attack()
player1.restore(100)
player1.decrease(20)
player1.showState(100, 30, "Helena")

jair = Player()
players.append(jair)
jair.showState(75, 20, "Jair")
print(players)
print(type(jair))