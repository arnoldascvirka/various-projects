class Kate:
    def __init__(self, spalva, kojos):
        self.spalva = spalva
        self.kojos = kojos

    def _judinti_kojas(self):
        pass

    def _ziureti_kur_begi(self):
        pass

    def begti(self):
        self._ziureti_kur_begi()
        self._judinti_kojas()
        print("Begu")


cat1 = Kate("Blue", 2)
cat1.begti()
