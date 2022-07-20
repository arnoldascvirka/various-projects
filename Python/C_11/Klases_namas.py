class Namas:
    def __init__(self, plotas, verte):
        self.plotas = plotas
        self.__verte = verte

    @property
    def verte(self):
        return self.__verte

    @verte.setter
    def verte(self, naujas):
        if isinstance(naujas, (float, int)) == True:
            if naujas > 0:
                self.__verte = naujas
            else:
                print("Verte turi buti daugiau nei 0")
        else:
            print("Verte privalo buti skaicius")

    @verte.deleter
    def verte(self):
        print("Istrinama")
        del self.__verte
        # Kaip panaudodoti?


namas = Namas(15, 15)

namas.verte = 20

print(namas.verte)

namas.verte = "AS1D"
