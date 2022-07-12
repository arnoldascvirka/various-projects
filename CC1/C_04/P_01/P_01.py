########################
#   Patikrina ar paso kodas teisingas
########################

pasas = str(input("Iveskinte asmens kodą: "))

def pasascheck(pasas: str) -> int:
    if len(pasas) == 11 and pasas[::-1].isdigit():
        print("Pasas teisingas")
    else:
        print("Pasas neteisingas")
    
pasascheck(pasas)

