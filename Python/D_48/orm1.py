    from sqlalchemy.orm import sessionmaker
from model import engine, Author

Session = sessionmaker(bind=engine)
session = Session()


# įrašymas .add()
#########################################################
# autorius1 = Author("Henry", "Miller", "german", 1908)
# session.add(autorius1)
#
# autorius2 = Author("Herman2", "Hesse2", "american", 1890)
# session.add(autorius2)

# session.commit()

# skaitymas .query
##############################################################
# eil = session.query(Author).get(1)
# print(eil)
# print(eil.f_name)
# print(eil.l_name)

visos_eilutes = session.query(Author).all()
print(visos_eilutes)
for eil in visos_eilutes:
    print(eil.f_name)
    print(eil.l_name)
    print(eil.y_born)

#filtras, jeigu rada daugiau nei 1, raisina Exceptioną
atfiltruota = session.query(Author).filter_by(f_name="Henry").one()
print(atfiltruota)

atfiltruota = session.query(Author).filter_by(natnl="american").all()
print(atfiltruota)

#lankstesnis filtras
atfiltruota = session.query(Author).filter(Author.f_name.ilike("H%")).all()
print(atfiltruota)
for eil in atfiltruota:
    print(eil.f_name)
    print(eil.l_name)
    print(eil.y_born)

print("*" * 50)

atfiltruota = session.query(Author).filter(Author.f_name.ilike("__r%")).all()
print(atfiltruota)
for eil in atfiltruota:
    print(eil.f_name)
    print(eil.l_name)
    print(eil.y_born)

print("*" * 50)

atfiltruota = session.query(Author).filter(Author.y_born < 1900).all()
print(atfiltruota)
for eil in atfiltruota:
    print(eil.f_name)
    print(eil.l_name)
    print(eil.y_born)

print("*" * 50)

atfiltruota = session.query(Author).filter(Author.y_born < 1900,
                                           Author.f_name.ilike("__r%")).all()
print(atfiltruota)
for eil in atfiltruota:
    print(eil.f_name)
    print(eil.l_name)
    print(eil.y_born)

# keitimas(update) .query
##############################################################
print("*" * 50)
autorius = session.query(Author).filter_by(f_name="Mark", l_name="Lutz").one()
print(autorius)
autorius.y_born = 1955
session.commit()
print(autorius)


# trynimas(delete)
print("*" * 50)
visos_eilutes = session.query(Author).all()
print(visos_eilutes)

autorius = session.query(Author).filter_by(f_name="Herman2").one()
print(autorius)
session.delete(autorius)
session.commit()

print("*" * 50)
visos_eilutes = session.query(Author).all()
print(visos_eilutes)
