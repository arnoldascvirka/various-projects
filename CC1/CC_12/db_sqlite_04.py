import sqlite3

conn = sqlite3.connect("duomenu_baze.db")
c = conn.cursor()

with conn:
    c.execute("UPDATE darbuotojai SET atlyginimas = 1000 WHERE pavarde = 'Sireika'")

    with conn:
        c.execute("SELECT * FROM darbuotojai")
        print(c.fetchall)
