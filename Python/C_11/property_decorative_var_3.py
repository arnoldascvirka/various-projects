class Darbuotas:
    def __init__(self, vardas, pavarde, atlyginimas):
        self.vardas = vardas
        self.pavarde = pavarde
        self.__atlyginimas = atlyginimas

    @property
    def atlyginimas(self):
        return self.__atlyginimas

    @atlyginimas.setter
    def atlyginimas(self, naujas):
        if naujas < 0:
            print("Atlyginimas negali buti neigiamas")
        else:
            self.__atlyginimas = naujas


domas = Darbuotas("Domantas", "Rutkauskas", 800)
print(domas.atlyginimas)

domas.atlyginimas = 100
print(domas.atlyginimas)
