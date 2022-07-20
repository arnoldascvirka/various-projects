import pickle

a = 111
b = 222
c = 333

with open("abc.pkl", "wb") as p_out:
    pickle.dump(a, p_out)
    pickle.dump(b, p_out)
    pickle.dump(c, p_out)

with open("abc.pkl", "rb") as p_in:
    print(pickle.load(p_in))
    print(pickle.load(p_in))
    print(pickle.load(p_in))

with open("abc.pkl", "rb") as p_in:
    while True:
        try:
            print(pickle.load(p_in))
        except EOFError:
            print("End of File")
            break
