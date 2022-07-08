# number = float(input("Type a natural number: "))
# try:
#     if number > 0: 
#         print("True")
#     else:
#         print("False")
# except:
#     print("Entry is not a number.")


########################
#   Prints the current date
########################

# from datetime import datetime, time

# time1 = datetime.today()
# time2 = datetime.today().time()
# print(time1)
# print(time2)


########################
#   Substracts or adds a date from the current date.
########################

import datetime
print('''Data-laikas, today''')
siandien = datetime.datetime.today()
print(siandien)
print("duomenų tipas: ", type(siandien), "\n")
print('''Data-laikas, išrenkam tik laiką''')
siandien2 = datetime.datetime.today().time()
print(siandien2)
print("duomenų tipas: ", type(siandien2), "\n")
print('''Data''')
siandien3 = datetime.date.today()
print(siandien3)
print("duomenų tipas: ", type(siandien3), "\n")
print('''įvedam datą-laiką, panaudodami atskirus parametrus
        - metai, mėnuo, diena ir tt''')
datalaikas = datetime.datetime(2022, 12, 31, 0, 45, 10)
print(datalaikas)
suformatuota = datalaikas.strftime("%A, %d %B %Y ")
print(suformatuota)
dabar = datetime.datetime.now()
print(dabar)
print("duomenų tipas: ", type(dabar))
print('''panaudojam timedelta days - dienų laiko skirtumą''')
skirtumas = datetime.timedelta(days=2)
print(dabar - skirtumas)
print(dabar + skirtumas)
print('''panaudojam timedelta hours - valandų laiko skirtumą''')
skirtumas = datetime.timedelta(hours=100)
print(dabar - skirtumas)
print(dabar + skirtumas)
print('''panaudojam timedelta ir hours ir days''')
skirtumas = datetime.timedelta(days=2, hours=5)
print(dabar - skirtumas)
print(dabar + skirtumas)
print('''panaudojam timedelta days, hours, minutes, seconds''')
skirtumas = datetime.timedelta(days=1, hours=5, minutes=20, seconds=50)
print(dabar - skirtumas)
print(dabar + skirtumas)
print('''panaudojam formatavimą iš vartotojo gauti datos įvedimą''')
ivestis = input("Įveskite datą YYYY-MM-DD HH:MM:SS formatu: ")
data = datetime.datetime.strptime(ivestis, "%Y-%m-%d %H:%M:%S")
print(type(data))
print('''apskaičiuojam skirtumą tarp dviejų datų''')
skirtumas = datetime.datetime.now() - data
print('''skirtume gaunam duomenų tipą:''')
print(type(skirtumas))
print("skirtumas yra: ", skirtumas)
