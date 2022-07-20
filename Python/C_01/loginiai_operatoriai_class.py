# class OO:
#    skaicius = int(input("Ivesti skaiciu: "))
#    skaicius2 = int(input("Ivesti skaiciu 2: "))
#    if(skaicius >= 10):
#        if(skaicius2 >= 10):
#            print("ivestas skaicius + skaicius2 = ", skaicius + skaicius2)
#        else:
#            print("ivestas skaicius - skaicius2 = ", skaicius - skaicius2)
#    else:
#        print("ivestas skaicius +10=", skaicius + 10)

# class AA:
#    a = int(input("Ivesti skaiciu: "))
#    b = int(input("Ivesti skaiciu 2: "))
#    if(a == b):
#        print("Skaičius a yra lygus b")
#    if(a > b):
#        print("Skaičius a yra didesnis už skaičių b")
#    if(a < b):
#        print("Skaičius a yra mažesnis už b")

# class BB:
#    num = int(input("Ivesti skaiciu:"))
#    if (num % 2) == 0:
#        print("Skaičius yra lygninis")
#    else:
#        print("Skaičius yra nelyginis")

# class CC:
#    a = "Zen of Python"
#    print(a[5])
#    print(a[7])
#    b = a.split(" ")
#    print(b[0])
#    print(b[2])
#    print(a[::-1])
#    print(b)
#    print(a.replace("Python", "Programming"))

# class DD:
#    a = "Zen of Python"
#    b = a.upper()
#    print (b)
#    c = a.casefold()
#    print(c)
#    d = a.capitalize()
#    print(d)
#    e = a.count("o")
#    print(e)
#    f = a.find("e")
#    print(f)


class EE:
    a = int(input("Įvesti skaičių: "))
    c = str(
        input(
            "Spauskite:\n+ kad prideti skaičių.\n- kad atimti skaičių.\n/ kad dalinti skaičių.\n* kad dauginti skaičių."
        )
    )
    if c == "+":
        b = int(input("Ivesti skaičių kurį pridėti: "))
        print("Rezultatas: ", a + b)
    if c == "-":
        b = int(input("Ivesti skaičių kurį atimti: "))
        print("Rezultatas: ", a - b)
    if c == "/":
        b = int(input("Ivesti skaičių iš kurio dalinti: "))
        print("Rezultatas: ", a / b)
    if c == "*":
        b = int(input("Ivesti skaičių su kuriuo dauginti: "))
        print("Rezultatas: ", a * b)
    else:
        print("Funkcija nepriimtina.")
