from televisores.tv import TV


class Control:
    def __init__(self, tv:TV):
        self._tv = tv

    def enlazar(self, tv:TV):
        self._tv = tv
    def turnOn(self):
        TV.turnOn

    def turnOff(self):
        TV.turnOff

    def canalUp(self):
        TV.canalUp
    
    def canalDown(self):
        TV.canalDown

    def volumenUp(self):
        TV.volumenUp

    def volumenDown(self):
        TV.volumenDown

    def setCanal(self):
        TV.setCanal

    def setVolumen(self):
        TV.setVolumen

    def setTv(self, tv:TV):
        self._tv = tv

    def getTv(self, tv:TV):
        return self._tv


        
