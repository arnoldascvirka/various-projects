from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Project01 import Project

engine = create_engine("sqlite:///project.db")
Session = sessionmaker(bind=engine)
session = Session()

project1 = session.query(Project).get(2)
print(project1.id, project1.name, project1.price)

project2 = session.query(Project).filter_by(name="ES edukacija")
for a in project2:
    print(a)
