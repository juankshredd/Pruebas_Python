# OO Dimmerswitch class

class DimmerSwitch():
    def __init__(self, label):
        self.switchIsOn = False
        self.brightness = 0
        self.label = label

    def turnOn(self):
        self.switchIsOn = True

    def turnOff(self):
        self.switchIsOn = False

    def raiseLevel(self):
        if self.brightness < 10:
            self.brightness = self.brightness + 1
    
    def lowerLevel(self):
        if self.brightness > 0:
            self.brightness = self.brightness - 1

    # Extra method for debugging
    def show(self):
        print('============================')
        print('Switch is on?\n', self.switchIsOn)
        print('Brightness level is: \n', self.brightness)
        print('Label: ', self.label)
        print('============================')

# Main code
# Create first DimmerSwitch, turn it on, and raise the level twice
oDimmer1 = DimmerSwitch(label= input('Enter Label for this device: \n'))
oDimmer1.turnOn()
oDimmer1.raiseLevel()
oDimmer1.raiseLevel()
# Create second DimmerSwitch, turn it on, and raise the level 3 times
oDimmer2 = DimmerSwitch(label= input('Enter Label for this device: \n'))
oDimmer2.turnOn()
oDimmer2.raiseLevel()
oDimmer2.raiseLevel()
oDimmer2.raiseLevel()
# Create third DimmerSwitch, using the default settings
oDimmer3 = DimmerSwitch(label= input('Enter Label for this device: \n'))
# Ask each switch to show itself
oDimmer1.show()
oDimmer2.show()
oDimmer3.show()