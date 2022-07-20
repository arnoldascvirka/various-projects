import pickle

a = 1024

########################
#   Iraso i pickle file
########################

with open("a.pkl", "wb") as p_out:
    pickle.dump(a, p_out)

########################
#   Istraukia is pickle file
#######################

with open("a.pkl", "rb") as p_in:
    print(pickle.load(p_in))

########################
#   Iraso zodyna i pickle file
########################

zodynas = {1: "Pirmas", 2: "Antras", 3: "Trecias"}

with open("b.pkl", "wb") as p_out:
    pickle.dump(zodynas, p_out)

########################
#   Istraukia zodynas is pickle file
########################

with open("b.pkl", "rb") as p_in:
    print(pickle.load(p_in))
