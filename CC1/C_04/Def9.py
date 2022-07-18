########################
#   Kviečia funkcija kuri patikrina ar data yra keliamieji metai
########################

import calendar


def leapyear(year):
    # Return the answer
    return bool(calendar.isleap(year))


year = int(input("Įveskite metus, kurie bus patikrinti ar tai keliamieji:"))
print(leapyear(year))
