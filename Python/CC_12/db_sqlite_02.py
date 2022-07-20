import sqlite3

conn = sqlite3.connect("duomenu_baze.db")

c = conn.cursor()

with conn:
    c.execute(
        """CREATE TABLE IF NOT EXISTS darbuotojai
            (vardas text, pavarde text, atlyginimas integer    
            )"""
    )

with conn:
    c.execute("INSERT INTO darbuotojai VALUES ('Arvydas', 'Sireika', 2000)")
    c.execute("INSERT INTO darbuotojai VALUES ('Ervydas', 'Sireika', 3500)")
