class Control:
    def enlazar(self, tv):
        self.setTv(tv)
        tv.setControl(self)

    def getTv(self):
        return self.tv

    def setTv(self, tv):
        self.tv = tv

    def turnOn(self):
        self.tv.turnOn()

    def turnOff(self):
        self.tv.turnOff()

    def canalUp(self):
        self.tv.canalUp()

    def canalDown(self):
        self.tv.canalDown()

    def volumenUp(self):
        self.tv.volumenUp()

    def volumenDown(self):
        self.tv.volumenDown()

    def setCanal(self, canal):
        if canal >= 1 and canal <=120: 
            self.tv.setCanal(canal)

    def setVolumen(self, volumen):
        if volumen >= 0 and volumen <=7:
            self.tv.setVolumen(volumen)




        
