########################
#   Kviečia funkcija kuri randa visus unikalius elementus
########################


def unique_elements(list1):
    unique = []
    for number in list1:
        if number not in unique:
            unique.append(number)

    return unique


list1 = input("Iveskite tai ko unikalus elementai bus isvesti: ")

print(unique_elements(list1))
