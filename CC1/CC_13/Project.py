import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///project.db")
Base = declarative_base()


class Project(Base):
    __tablename__ = "Project"
    id = Column(Integer, primary_key=True)
    name = Column("Name", String)
    price = Column("Price", Float)
    created_date = Column("Date created", DateTime, default=datetime.datetime.utcnow)

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.id} {self.name} - {self.price}: {self.created_date}"


Base.metadata.create_all(engine)
