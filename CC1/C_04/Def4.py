########################
#   Kviečia funkcija kuri atspausdina žodį atbulai
########################

def reverse(a: str) -> str:
    return a[::-1]

a = input("Įveskite žodį kuris bus gražintas atbulai: ")

print(reverse(a))