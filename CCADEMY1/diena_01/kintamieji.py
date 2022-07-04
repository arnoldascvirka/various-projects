a = 10
a = a + 5

print (a)

a += 2
print("Reikšmė:", a)

a **= 3
print("Pakėlus 3 laipsniu a, reikšmė:", a)

a /= 100
print("Padalinus a iš 100, reikšmė:", a)

b = 13
sveika_dalis = b // 2
print(b, "sveika dalis padalinus iš 2, reikšmė:", sveika_dalis) 

dalybos_liekana = b % 2
print (b, "dalybos liekana padalinus iš 2, reikšmė", dalybos_liekana)

vartotojas_ivede = input("Ivesk ->")
print("Tai ką įvedei *3 yra:", int(vartotojas_ivede)     * 3)