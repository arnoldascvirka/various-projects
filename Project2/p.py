import sqlite3

######## SQLITE DATABASE SETUP #########
# create sqlite database in RAM
db = sqlite3.connect("QnA.db")

# get a cursor object. we will use the cursor to pass sql statements
cursor = db.cursor()


print("\n>Quiz zaidimas.\n")

q_numb = 0
t_numb = 0

while True:
    q_numb += 1
    # select a random row from the database

    # ORDER BY RANDOM()
    cursor.execute("""SELECT * FROM Questions LIMIT 1""")
    question = ""
    for row in cursor:
        question = row[1]

    cursor.execute("""SELECT * FROM Choices LIMIT 1""")
    choice = ""
    for row in cursor:
        choice = row[1]

    # print question
    print(">Question %d: %s" % (q_numb, question))
    user_choice = input("> ")
    if user_choice.lower() == choice.lower():
        print("That's right!")
        t_numb += 1
    elif user_choice.lower() == "quit":
        print()
        print("Quitting game.")
        q_numb -= 1
        break
    else:
        print("Sorry. The correct answer is: %s" % choice)
    print("Score: %d/%d" % (t_numb, q_numb))
    print()

final = 0
if q_numb != 0:
    final = (t_numb * 100) / q_numb
print("\nFinal Score: %d%% (%d/%d)" % (final, t_numb, q_numb), "\n")

# close sqlite database
db.close()
