from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///biblioteka2.db')
Base = declarative_base()


class Author(Base):
    __tablename__ = "author"
    id = Column(Integer, primary_key=True)
    f_name = Column("fname", String)
    l_name = Column("lname", String)
    natnl = Column("nationality", String)
    y_born = Column("yearborn", Integer)
    y_died = Column("yeardied", Integer)
    bio = Column("biography", String)
    books = relationship("Book")

    def __init__(self, f_name, l_name, natnl, y_born, y_died=None, bio=None):
        self.f_name = f_name
        self.l_name = l_name
        self.natnl = natnl
        self.y_born = y_born
        self.y_died = y_died
        self.bio = bio

    def __repr__(self):
        return f"{self.f_name} {self.l_name}, {self.natnl}, {self.y_born}"


class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True)
    b_title = Column("btitle", String)
    nr_isbn = Column("nrisbn", String)
    b_year = Column("byear", Integer)
    author_id = Column(Integer, ForeignKey("author.id"))
    auth = relationship("Author")

    def __init__(self, b_title, nr_isbn, b_year):
        self.b_title = b_title
        self.nr_isbn = nr_isbn
        self.b_year = b_year

    def __repr__(self):
        return f"{self.b_title} - {self.nr_isbn} - {self.b_year}"


Base.metadata.create_all(engine)

