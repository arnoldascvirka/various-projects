from cgitb import text
import sqlite3

conn = sqlite3.connect("duomenu_baze.db")
c = conn.cursor()

c.execute(
    """CREATE TABLE IF NOT EXIST darbuotojai (
        vardas text,
        pavarde text,
        atlyginimas integer,
        )"""
)

conn.commit()
conn.close()
