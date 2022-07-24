import sqlite3

conn = sqlite3.connect("duomenu_baze.db")

c = conn.cursor()

with conn:
    c.execute(
        """CREATE TABLE IF NOT EXISTS darbuotojai
            (vardas text, pavarde text, atlyginimas integer    
            )"""
    )

while True:
    print("Iveskite darbuotoja")
    vardas = input("Vardas: ")
    pavarde = input("Pavarde: ")
    atlyginimas = int(input("Atlyginimas: "))

    with conn:
        c.execute(
            f"INSERT INTO darbuotojai VALUES ('{vardas}', '{pavarde}', '{atlyginimas}')"
        )

    with conn:
        c.execute("SELECT * FROM darbuotojai")
        for rec in c.fetchall():
            print(rec)
