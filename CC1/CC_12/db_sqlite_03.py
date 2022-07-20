import sqlite3

conn = sqlite3.connect("duomenu_baze.db")
c = conn.cursor()

with conn:
    c.execute("SELECT * FROM darbuotojai WHERE vardas = 'Ervydas'")
    print(c.fetchall())
