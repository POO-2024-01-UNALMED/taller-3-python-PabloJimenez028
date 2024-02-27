from televisores.tv import TV
class Control:
    def __init__(self):
        self._tv = None

    def enlazar(self, tv):
        self._tv = tv
        TV.setControl = tv

    def setTv(self, tv):
        self._tv = tv

    def getTv(self):
        return self._tv
    
    
    def turnOn(self):
        self.turnOn()

    def turnOff(self):
        self.turnOff()

    def canalUp(self):
        self.canalUp()
    
    def canalDown(self):
        self.canalDown()

    def volumenUp(self):
        self.volumenUp()

    def volumenDown(self):
        self.volumenDown()

    def setCanal(self, canal):
        self.setCanal(canal)

    def setVolumen(self, volumen):
        self.setVolumen(volumen)
        




        
