class Darbuotas:
    def __init__(self, vardas, pavarde, atlyginimas):
        self.vardas = vardas
        self.pavarde = pavarde
        self.__atlyginimas = atlyginimas

    def set_atlyginimas(self, naujas):
        if naujas < 0:
            print("Atlyginimas negali buti neigiamas")
        else:
            self.__atlyginimas = naujas

    def get_atlyginimas(self):
        return self.__atlyginimas


domas = Darbuotas("Domas", "Rutkauskas", 800)
print(domas.get_atlyginimas())


domas.atlyginimas = 500
print(domas.get_atlyginimas())


print(domas.get_atlyginimas())
