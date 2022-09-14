from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///many2many.db')
Base = declarative_base()

association_table = Table("association", Base.metadata,
                          Column('tevas_id', Integer, ForeignKey('tevas.id')),
                          Column('vaikas_id', Integer, ForeignKey('vaikas.id')))


class Tevas(Base):
    __tablename__ = 'tevas'
    id = Column(Integer, primary_key=True)
    vardas = Column("vardasdb", String)
    pavarde = Column("pavardedb", String)
    vaikai = relationship("Vaikas", secondary=association_table, back_populates="tevai")


class Vaikas(Base):
    __tablename__ = 'vaikas'
    id = Column(Integer, primary_key=True)
    vardas = Column("vardasdb", String)
    pavarde = Column("pavardedb", String)
    tevai = relationship("Tevas", secondary=association_table, back_populates="vaikai")


Base.metadata.create_all(engine)
