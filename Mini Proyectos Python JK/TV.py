# TV class
class TV():
    def __init__(self):
        self.isOn = False
        self.isMuted = False
        # Some default list of channels
        self.channelList = [2, 4, 5, 7, 9, 11, 20, 36, 44, 54, 65]
        self.nChannels = len(self.channelList)
        self.channelIndex = 0
        self.VOLUME_MAXIMUM = 10
        self.VOLUME_MINIMUM = 0
        self.volume =0 #// # Integer divide *** EN ESTA LINEA FALTA ALGO EN EL LIBRO PARA ESTA DIVISION A ENTERO ***
    
    def power(self):
        self.isOn = not self.isOn # toggle

    def volumeUp(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False # ChangiNg the volume while muted unmutes the sound
        if self.volume < self.VOLUME_MAXIMUM:
            self.volume = self.volume + 1

    def volumeDown(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False # changing the volume while muted unmutes the sound
        if self.volume > self.VOLUME_MINIMUM:
            self.volume = self.volume - 1
    
    def channelUp(self):
        if not self.isOn:
            return
        self.channelIndex = self.channelIndex + 1
        if self.channelIndex > self.nChannels: 
            self.channelIndex = 0  # Wrap around to the first channel

    def channelDown(self):
        if not self.isOn:
            return
        self.channelIndex = self.channelIndex - 1
        if self.channelIndex < 0:
            self.channelIndex = self.nChannels - 1 # wrap around to the top channel

    def mute(self):
        if not self.isOn:
            return
        self.isMuted = not self.isMuted

    def setChannel(self, newChannel):
        if newChannel in self.channelList:
            self.channelIndex = self.channelList.index(newChannel)
            # if the newChannel is not in our list of channels, don't do anything

    def showInfo(self):
        print('============================')
        print('         TV STATUS          ')
        if self.isOn:
            print('       TV is ON        ')
            print('       CHANNEL is: ', self.channelList[self.channelIndex])
            if self.isMuted:
                print('      Volume is: ', self.volume, '(sound is muted)')
            else:
                print('     Volume is: ', self.volume)
        else:
            print('          TV is: Off')

# # Main code
# oTV = TV() # create the TV object
# # Turn the TV on and show the status
# oTV.power()
# oTV.showInfo()
# # Change the channel up twice, raise the volume twice, show status
# oTV.channelUp()
# oTV.channelUp()
# oTV.volumeUp()
# oTV.volumeUp()
# oTV.showInfo()
# # Turn the TV off, show status, turn the TV on, show status
# oTV.power()
# oTV.showInfo()
# oTV.power()
# oTV.showInfo()
# # Lower the volume, mute the sound, show status
# oTV.volumeDown()
# oTV.mute()
# oTV.showInfo()
# # Change the channel to 11, mute the sound, show status
# oTV.setChannel(11)

# oTV.mute()
# oTV.showInfo()

# Main code
oTV1 = TV() # create one TV object
oTV2 = TV() # create another TV object

# Turn both TVs on
oTV1.power()
oTV2.power()
# Raise the volume of TV1
oTV1.volumeUp()
oTV1.volumeUp()
# Raise the volume of TV2
oTV2.volumeUp()
oTV2.volumeUp()
oTV2.volumeUp()
oTV2.volumeUp()
oTV2.volumeUp()
# Change TV2's channel, then mute it
oTV2.setChannel(44)
oTV2.mute()
# Now display both TVs
oTV1.showInfo()
oTV2.showInfo()
