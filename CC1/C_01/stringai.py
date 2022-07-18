# Šiame faile mokinsimės veiksmų su stringais, indeksavimo ir string metodų

s = "CodeAcademy"
print(s[0])
print(s[4])

print(s[0] + s[4])


# Slice operation.

print(s[0:4])

print(s[4:11])

print(s[0:-0])

print(s.replace("Academy", "Akademija"))

print(s.replace("a", ""))

print(s.upper())

print(s.lower())

d = "sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque"

print(d.capitalize())

print(d.strip())

l = d.split(" ")
print(l[5])
print("čia išdalintas stringas saraše:  ", l)
print("Čia sujungtas vėl:   ", " ".join(l))
