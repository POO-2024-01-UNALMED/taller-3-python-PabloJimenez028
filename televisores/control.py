class Control:
    def enlazar(self, tv):
        self.setTv(tv)
        tv.setControl(self)

    def setTv(self, tv):
        self.tv = tv

    def getTv(self):
        return self.tv
    
    
    def turnOn(self):
        self.tv.turnOn(self)

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
        self.tv.setCanal(canal)

    def setVolumen(self, volumen):
        self.tv.setVolumen(volumen)




        
