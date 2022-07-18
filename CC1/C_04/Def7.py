########################
#   Kviečia funkcija kuri patikrina ar numeris yra pirminis
########################


def isPrime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


n = int(input("Įveskite skaičių, kuris bus patikrintas ar tai pirminis: "))

print(isPrime(n))
