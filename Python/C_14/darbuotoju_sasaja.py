from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from darbuotojai import Darboutojai


engine = create_engine("sqlite:///darbuotojai.db")
Session = sessionmaker(bind=engine)
session = Session()

##################################################

while True:
    try:
        choice = int(
            input(
                """Pick:
        1 - Show all projects
        2 - Create project
        3 - Change project
        4 - Delete project
        5 - Exit program
        \n"""
            )
        )

        if choice == 1:
            projects = session.query(Darboutojai).all()
            print("#####################")
            for a in projects:
                print(a)
            print("#####################")

        if choice == 2:
            try:
                vardas = input("Enter name: ")
                pavarde = input("Enter last name: ")
                gimimo_data = datetime.strptime(
                    input("Enter date of birth (YYYY-MM-DD): "), "%Y-%m-%d"
                )
                pareigos = input("Enter qualification: ")
                atlyginimas = input("Enter salary: ")
                project2 = Darboutojai(
                    vardas, pavarde, gimimo_data, pareigos, atlyginimas
                )
                session.add(project2)
                session.commit()
            except:
                print("Wrong entry.")

        if choice == 3:
            projects = session.query(Darboutojai).all()
            print("#####################")
            for a in projects:
                print(a)
            print("#####################")
            try:
                changed_id = input("Choose ID: ")
                changed_project = session.query(Darboutojai).get(changed_id)
                choice = int(
                    input(
                        "1 - Change name\n2 - Change last name\n"
                        "3 - Change date of birth\n4 - Change qualification\n"
                        "5 - Change salary\n"
                    )
                )
                if choice == 1:
                    changed_project.vardas = input("Enter name: ")
                elif choice == 2:
                    changed_project.pavarde = input("Enter last name: ")
                elif choice == 3:
                    changed_project.gimimo_data = datetime.strptime(
                        input("Enter date of birth (YYYY-MM-DD: ): "), "%Y-%m-%d"
                    )
                elif choice == 4:
                    changed_project.pareigos = input("Enter qualification: ")
                elif choice == 5:
                    changed_project.atlyginimas = input("Enter salary: ")
                else:
                    print("Wrong entry.")
            except:
                print("Wrong entry.")

        if choice == 4:
            projects = session.query(Darboutojai).all()
            print("#####################")
            for a in projects:
                print(a)
            print("#####################")
            changed_id = int(input("Choose ID: "))
            deleted_project = session.query(Darboutojai).get(changed_id)
            session.delete(deleted_project)
            session.commit()

        if choice == 5:
            break
    except:
        print("Wrong entry")
