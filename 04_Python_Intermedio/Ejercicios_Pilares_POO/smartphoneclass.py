from phoneclass import Phone
from cameraclasss import Camera

class Smartphone(Camera, Phone):

    def turn_on(self):
        print("Teléfono encendido")