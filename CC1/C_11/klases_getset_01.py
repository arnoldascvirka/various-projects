class Darbuotas:
    def __init__(self, vardas, pavarde, atlyginimas):
        self.vardas = vardas
        self.pavarde = pavarde
        self.atlyginimas = atlyginimas


domas = Darbuotas("Domas", "Rutkauskas", 800)
print(domas.atlyginimas)
print("\nSet domas.atlyginimas 1500\n")
domas.atlyginimas = 1500
print(domas.atlyginimas)

donatas = Darbuotas("Donatas", "Kazlauskas", 800)
donatas.atlyginimas = -2000
print(donatas.atlyginimas)
