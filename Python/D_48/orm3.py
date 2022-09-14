from sqlalchemy.orm import sessionmaker

from model3 import engine, Tevas, Vaikas

Session = sessionmaker(bind=engine)
session = Session()

# # įrašų sukūrimas
# tevas1 = Tevas(vardas="Tėvas1", pavarde="Tėvauskas1")
# tevas2 = Tevas(vardas="Motina1", pavarde="Motinauskienė1")
# tevas3 = Tevas(vardas="Tėvas3", pavarde="Tėvauskas3")
# vaikas1 = Vaikas(vardas="Vaikas1", pavarde="Tėvaika1")
# vaikas2 = Vaikas(vardas="Vaikas1", pavarde="Tėvaikytė1")

# tevas1.vaikai.append(vaikas1)
# tevas2.vaikai.append(vaikas1)
# tevas2.vaikai.append(vaikas2)
# tevas3.vaikai.append(vaikas2)

# session.add(tevas1)
# session.add(tevas2)
# session.add(tevas3)
# session.commit()


tevas = session.query(Tevas).get(2)  # tevas su id 2
print("\n", tevas.vardas, tevas.pavarde)
for vaikas in tevas.vaikai:
    print(vaikas.vardas, vaikas.pavarde)

vaikas = session.query(Vaikas).get(1)  # vaikas su id 1
print("\n", vaikas.vardas, vaikas.pavarde)
for tevas in vaikas.tevai:
    print(tevas.vardas, tevas.pavarde)

# visi įrašai iš tėvų pusės
print("*" * 50)
tevai = session.query(Tevas).all()  # visi tevai
for tevas in tevai:
    print("\n", tevas.vardas, tevas.pavarde)
    for vaikas in tevas.vaikai:
        print(vaikas.vardas, vaikas.pavarde)

# visi įrašai iš vaikų pusės
print("*" * 50)
vaikai = session.query(Vaikas).all()  # visi vaikai
for vaikas in vaikai:
    print("\n", vaikas.vardas, vaikas.pavarde)
    for tevas in vaikas.tevai:
        print(tevas.vardas, tevas.pavarde)

# įrašo keitimas
tevas = session.query(Tevas).get(1)
print(tevas.vardas)
tevas.vardas = "Naujasvardas"
session.commit()
print(tevas.vardas)

print(tevas.vaikai[0].vardas)
tevas.vaikai[0].vardas = "NaujasVaikoVardas"
session.commit()
print(tevas.vaikai[0].vardas)

print("VISI: ", tevas.vaikai)

# vaiko ištrynimas iš tėvo

tevas.vaikai.remove(tevas.vaikai[0])
print("VISI: ", tevas.vaikai)
print(type(tevas.vaikai))
