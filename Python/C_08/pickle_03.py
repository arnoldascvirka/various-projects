import pickle


class Automobilis:
    def __init__(self, modelis, marke="Toyota", kuro_tipas="Benzinas"):
        self.marke = marke
        self.modelis = modelis
        self.kuro_tipas = kuro_tipas


Automobiliai = [Automobilis("Avensis"), Automobilis("Corolla"), Automobilis("Supra")]


with open("automobiliai.pkl", "wb") as p_out:
    pickle.dump(Automobiliai, p_out)

with open("automobiliai.pkl", "rb") as p_in:
    automobiliai2 = pickle.load(p_in)
    for automobilis in automobiliai2:
        print("Marke:      ", automobilis.marke)
        print("Modelis:    ", automobilis.modelis)
        print("Kuro tipas: ", automobilis.kuro_tipas)
        print("\n")
