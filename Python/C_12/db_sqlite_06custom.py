import sqlite3

conn = sqlite3.connect("duomenu_baze2.db")

c = conn.cursor()

with conn:
    c.execute(
        """CREATE TABLE IF NOT EXISTS paskaitos
            (
                pavadinimas text, destytojas text, trukme integer    
            )"""
    )


# Adds multiple values to the base
##########################################################################
#
# with conn:
#     c.execute("INSERT INTO paskaitos VALUES ('Vadyba', 'Domantas', 40)")
#     c.execute("INSERT INTO paskaitos VALUES ('Java', 'Tomas', 80)")
#     c.execute("INSERT INTO paskaitos VALUES ('Python', 'Donatas', 80)")


# Shows all results where the length is over 50
##########################################################################
#
# with conn:
#     c.execute("SELECT * FROM paskaitos WHERE trukme > 50")
#     for rec in c.fetchall():
#         print(rec)


# Updates "Python" to "Python programming"
#########################################################################
# #
# with conn:
#     c.execute(
#         "UPDATE paskaitos SET pavadinimas = 'Python programavimas' WHERE pavadinimas = 'Python'"
#     )


# Deletes paskaita where the instructor is Tomas
#########################################################################
#
# with conn:
#    c.execute("DELETE from paskaitos WHERE destytojas = 'Tomas'")

# Displays the whole table
#########################################################################
#
with conn:
    c.execute("SELECT * FROM paskaitos")
    for rec in c.fetchall():
        print(rec)
