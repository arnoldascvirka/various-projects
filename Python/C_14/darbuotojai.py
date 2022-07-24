from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///darbuotojai.db")
Base = declarative_base()

#########################


class Darboutojai(Base):
    __tablename__ = "Darbuotojai"
    id = Column(Integer, primary_key=True)
    vardas = Column("Name", String)
    pavarde = Column("Last name", String)
    gimimo_data = Column("Date of birth", DateTime)
    pareigos = Column("Qualification", String)
    atlyginimas = Column("Salary", Integer)
    darbo_pradzia = Column("Start of work", DateTime, default=datetime.utcnow)

    def __init__(
        self,
        vardas,
        pavarde,
        gimimo_data,
        pareigos,
        atlyginimas,
    ):
        self.vardas = vardas
        self.pavarde = pavarde
        self.gimimo_data = gimimo_data
        self.pareigos = pareigos
        self.atlyginimas = atlyginimas

    def __repr__(self):
        return f"{self.id}: {self.vardas}, {self.pavarde}, {self.gimimo_data}, {self.pareigos}, {self.atlyginimas}, {self.darbo_pradzia}"


Base.metadata.create_all(engine)
