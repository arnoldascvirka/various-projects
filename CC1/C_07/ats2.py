import datetime

with open("tekstas", "a") as byla:
    siandien = datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S")

    byla.write("\n")
    byla.write(siandien)

with open("tekstas", "r") as f:
    print(f.read())
