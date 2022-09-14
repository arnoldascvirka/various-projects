#####################################################
# Importing libraries
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

#####################################################

engine = create_engine("sqlite:///biblioteka.db")
Base = declarative_base()

#####################################################


class Asmuo(Base):
    __tablename__ = "asmuo"
    id = Column(Integer, primary_key=True)
    f_name = Column("name", String)
    l_name = Column("last name", String)
    pin_code = Column("personal number", Integer)
    p_num = Column("phone number", Integer)

    #################################

    child = relationship("Balance", back_populates="parent")

    #################################

    def __init__(self, f_name, l_name, p_num):
        self.f_name = f_name
        self.l_name = l_name
        # self.pin_code = pin_code
        self.p_num = p_num

    def __repr__(self):
        return f"{self.f_name} {self.l_name}, {self.p_num}"


class Bankas(Base):
    __tablename__ = "bankas"
    id = Column(Integer, primary_key=True)
    name = Column("name", String)
    adresas = Column("adresas", String)
    b_code = Column("banko kodas", String)
    swift = Column("SWIFT", Integer)

    #################################

    child = relationship("Balance", back_populates="parent")

    #################################

    def __init__(self, name, adresas, b_code, swift):
        self.name = name
        self.adresas = adresas
        self.b_code = b_code
        self.swift = swift

    def __repr__(self):
        return f"{self.name} {self.adresas}, {self.b_code}, {self.swift}"


class Balance(Base):
    __tablename__ = "bankas"
    id = Column(Integer, primary_key=True)
    number = Column("name", String)
    balance = Column("balance", String)

    #################################

    child = relationship("Balance", back_populates="parent")

    #################################

    def __init__(self, number, balance):
        self.number = number
        self.balance = balance

    def __repr__(self):
        return f"{self.number} {self.balance}"


Base.metadata.create_all(engine)

#####################################################
