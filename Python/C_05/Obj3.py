class Irasas:
    def __init__(self, tipas, suma):
        self.tipas = tipas
        self.suma = suma

    def __str__(self):
        return f"{self.tipas}: {self.suma}€"


class Biudzetas:
    def __init__(self):
        self.zurnalas = []

    def prideti_pajamu_irasa(self, pajamos):
        irasas = Irasas("Pajamos", pajamos)
        self.zurnalas.append(irasas)

    def prideti_islaidu_irasa(self, islaidos):
        irasas = Irasas("Išlaidos", islaidos)
        self.zurnalas.append(irasas)

    def gauti_balansa(self):
        suma = 0
        for i in self.zurnalas:
            if i.tipas == "Pajamos":
                suma += i.suma
            if i.tipas == "Išlaidos":
                suma -= i.suma
        return suma

    def grazinimas(self):
        for i in self.zurnalas:
            return i


biudzetas = Biudzetas()
while True:
    pasirinkimas = int(
        input(
            f"1 - Įvesti pajamas\n2 - Įvesti išlaidas\n3 - Parodyti pajamų / išlaidų balansą\n"
            f"4 - Parodyti biudžeto ataskaitą\n5 - Išeiti iš programos\n"
        )
    )
    if pasirinkimas == 1:
        pajamos = int(input("Įveskite pajamų sumą: "))
        biudzetas.prideti_pajamu_irasa(pajamos)
    elif pasirinkimas == 2:
        islaidos = int(input("Įveskite išlaidų sumą: "))
        biudzetas.prideti_islaidu_irasa(islaidos)
    elif pasirinkimas == 3:
        print(f"Sąskaitos balansas yra: {biudzetas.gauti_balansa()}€")
    elif pasirinkimas == 4:
        print(biudzetas.grazinimas())
    elif pasirinkimas == 5:
        print("Programa išjungiama")
        break
    else:
        print("Neteisingai įvesta. Įveskite 1-4")
