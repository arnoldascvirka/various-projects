class Kate:
    def __init__(self, spalva, kojos):
        self.spalva = spalva
        self.kojos = kojos

    def sayMiau(self):
        print("Miau")


cat1 = Kate("Blue", 2)
cat2 = Kate("Red", 4)

print(cat1.kojos)
cat1.sayMiau()
