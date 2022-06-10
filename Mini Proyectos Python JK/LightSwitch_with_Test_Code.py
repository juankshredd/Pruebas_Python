# OO_LightSwitch

class LightSwitch():
# Este es el constructor o inicializador, este corre cuando se crea una instancia
# Inicializa un switch apagado
    def __init__(self):
        self.switchIsOn = False

# Estos son los metodos de la clase

    def turnOn(self):
        # Enciende el switch
        self.switchIsOn = True

    def turnOff(self):
        # Apaga el switch
        self.switchIsOn = False

    def show(self):
        # Muestra el estado del switch
        print(self.switchIsOn)

# Se crea un objeto de la clase
oLightSwitch = LightSwitch()
oLightSwitch1 = LightSwitch()

# Se llaman sus metodos
oLightSwitch.show()
oLightSwitch.turnOn()
oLightSwitch.show()
oLightSwitch.turnOff()
oLightSwitch.show()
print('============================')
oLightSwitch1.show()
oLightSwitch1.turnOn()
oLightSwitch1.show()
