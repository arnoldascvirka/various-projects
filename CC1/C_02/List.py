# List1 = [] #Empty list 
# print(List1)
# ListINT = [1, 25, 50, 75, 100, 12, 2,5]
# print(ListINT)
# ListSTR = ["Autumn", "Winter", "Spring", "Summer"]
# print(ListSTR)
# ListMIX = [25, 50, "One", "Two"]
# print(ListMIX)

# ListCPLEX =  ["One, Two", 5, 10, 15, [ "Three, Four", 88, 99, 111 ]]
# print(ListCPLEX)

# card = [["Martynas Martinaintis", 1982, "Valytojas"],
#         ["Jonas Petraitis", 1993, "Vairuotojas"]]
# print(ListINT[1])
# print(ListSTR[-1])
# print(ListMIX[1:3])

#ŽODYNAI dict
# d = {}
# print(d)
# d = {'Andrius': 28, 'Jonas': 25, 'Ugne': 20}
# print(d)
# # išrenkam elementą iš žodyno(jo value) pagal raktą(key)
# print(d['Jonas'])
# # papildom nauja raktas:reikšmė pora žodyną
# d['Aloyzas'] = 68
# print(d)
# # trynimas iš žodyno
# del d['Aloyzas']
# print(d)

sarasas_sk = [1, 25, 78, 89, 74, 14.2, 12]
sarasas_str = ["0ruduo", "1ziema", "2pavasaris", "3vasara"]
#perrenkam cikle kiekvieną sąrašo elementą
# ir atliekam su juo veiksmus
for _ in sarasas_sk:
    print(_ * 1000)
for eil in sarasas_str:
    print(eil)
    print(eil[1:].upper(), "\n") #atskiriam naujos eil simboliu
#sumuojam skaičius sąraše
suma = 0
for sk in sarasas_sk:
    suma = suma + sk
    print(suma)
print("*" * 30)
#for ciklas su sąlygos panaudojimu
# skaičius mažesnius už 50 atspausdinam padaugintus iš 100
for sk in sarasas_sk:
    if sk < 50:
        print(sk * 100)
    else:
        print(sk)
print("ŽODYNAI", "*" * 20)
#perrenkam žodynus cikle for
d = {'Andrius': 28, 'Jonas': 25, 'Ugne': 20}
#perrenkam raktus
for elem in d:
    print(elem)
# perrenkam raktus ir pagal raktą reikšmę
for elem in d:
    print(elem, d[elem])
# perrenkam reikšmes value()
for val in d.values():
    print(val)
# perrenkam poromis items()
for k, v in d.items():
    print(k, v)
# funkcija range
for number in range(20):
    print(number)
for number in range(5, 16):
    print(number)
ilgas_sarasas = sarasas_sk * 10
print(ilgas_sarasas)
print(len(ilgas_sarasas))
for index in range(5, 15):
    print(index, ilgas_sarasas[index])
# range su žingsniu 2
for number in range(1, 20, 2):
    print(number)
print("WHILE ciklas", "*" * 20)
# ciklas WHILE - kol
a = 5
while a < 100:
    a += 5
    print(a)
print("programa išėjo iš ciklo while")
# BREAK - ciklo nutraukimo statementas
for nr in range(0, 10, 2):
    print(nr)
    if nr == 6: #ciklo nutraukimo sąlyga
        print("range pasiekė 6, nutraukiam ciklą pagal sąlygą")
        break #nutraukia ciklo vykdymą
# BREAK while cikle
nr = 0
while True:
    print(nr)
    nr += 2
    if nr > 6:
        print("ciklas pasiekė 6")
        break
