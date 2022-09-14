#####################################################

# Importing libraries
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Importing modules
from model1 import engine

#####################################################

Session = sessionmaker(bind=engine)
session = Session()

#####################################################
# Manually add entries to the table
# a1 = Author("William", "Shakespeare", "UK", 1582, 1613)
# session.add(a1)

# a2 = Author("Agatha", "Christie", "UK", 1890, 1973)
# session.add(a2)

# a3 = Author("Eiichiro", "Oda", "Japan", 1975, 1994)
# session.add(a3)

# a4 = Author("Georges", "Simenon", "French", 1903, 1989)
# session.add(a4)

# a5 = Author("Leo", "Tolstoy", "Russian", 1828, 1910)
# session.add(a5)

# session.commit()

#####################################################
# Show all entries in the table
# e = session.query(Author).all()
# print(e)

# Show all entries in the table with loop
# for ei in e:
#     print(f"{ei.f_name} {ei.l_name} {ei.y_born}")

#####################################################
#
def start():
    print()
    print("#################################")
    print()
    print("  Welcome to the bank system.")
    print()
    print("#################################")
    print()
    print("  Press 1 to enter a new user.")
    print("  Press 2 to enter a new bank.")
    print()
    print("#################################")
    print()


start()

choice = input("")
