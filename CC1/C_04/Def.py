########################
#   Kviečia funkcija kuri prideda 3 duotus skaičius
########################


def d(number1: int, number2: int, number3: int) -> int:
    return number1 + number2 + number3


try:
    number1 = int(input("Pirmas skaičius: "))
    number2 = int(input("Antras skaičius: "))
    number3 = int(input("Trečias skaičius: "))
    print(d(number1, number2, number3))
except:
    print("Not printable.")
