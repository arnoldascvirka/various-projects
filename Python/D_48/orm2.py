from sqlalchemy.orm import sessionmaker
from model2 import engine, Author, Book

Session = sessionmaker(bind=engine)
session = Session()

# įrašų kūrimas
################################################################
book1 = Book("Learning Python", "ISBN78956541", 2014)
book2 = Book("Programming with Python", "ISBN321654", 2012)

author = Author("Mark", "Lutz", "american", 1955)

author.books.append(book1)
author.books.append(book2)

session.add(author)
session.commit()

## įrašų nuskaitymas
################################################################
author = session.query(Author).get(1)
print(author)
print(author.books)
for b in author.books:
    print(b.b_title)
    print(b.b_year)

visi_autoriai = session.query(Author).all()

author.books[0].b_year = 2015
print(author.books)


## ryšio pašalinimas
#################################################################
author.books.remove(author.books[0])


author = session.query(Author).get(1)
print(author)
print(author.books)
