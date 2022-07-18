import pickle

listas = []

with open("listas1.pkl", "wb") as f:
    pickle.dump(listas, f)


def trim(n):
    n = n.replace("+", "")
    n = int(n)

    with open("listas1.pkl", "rb") as f:

        new_listas = pickle.load(f)

        new_listas.append(n)

    with open("listas1.pkl", "wb") as f:
        pickle.dump(new_listas, f)

    with open("listas1.pkl", "rb") as f:
        print(pickle.load(f))


while True:

    n = str(
        input(
            "Pridekite pajamas su '+ (Numeris)' arba atimkite islaidas su '- (Numeris)': "
        )
    )

    try:
        if n.find("+"):
            trim(n)
        elif n.find("-"):
            trim(n)
    except:
        print("Neteisingai įvesta.")

    if input("\nContinue?\nPress N to exit.\nPress any key to continue.\n") == "n":
        break

# a class that derives a function from titself.
