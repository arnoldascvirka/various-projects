with open("testinis", "w") as f:
    f.write("01234")
    f.seek(2)
    f.write("A")
    
with open("testinis", "r") as f:
    print(f.read())