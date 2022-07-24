class Player:
    def _init_(self, health, power, name):
        self.health = health
        self.power = power
        self.name = name
    def attack(self):
        for i in range(10):
            print("bullet attack!!!")
    def restore(self, health):
        health += 1
        print(f"health restored to {health}")
        return health
    def decrease(self, health):
        health -= 1
        print(f"health decreased to {health}")
        return health
    def showState(self, health, power, name):
        print("** PLAYER ***")
        print("** STATUS ***")
        print(f"player name : {name}")
        print(f"player power : {power}")
        print(f"player health : {health}")
        print("***======**")
        