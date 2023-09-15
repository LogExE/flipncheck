import sqlite3
from random import choices

con = sqlite3.connect("scores.db")
cur = con.cursor()

mults = {0.2: 0.1, 0.5: 0.3, 1: 0.2, 2: 0.3, 10: 0.1}

s = 1

print(
    f"You have 1 dollar. Each turn you will flip a {len(mults)}-sided coin to multiply the amount."
)

print("Multipliers are:")
for mult, prob in mults.items():
    print(f"x{mult} with probability {prob}")

print('We\'re playing until you type "done"')
while True:
    try:
        ans = input()
    except EOFError:
        print("done")
        break
    if ans == "done":
        break
    m = choices(list(mults.keys()), list(mults.values()))[0]
    print(f"Rolled x{m}")
    s *= m
    print(f"Now you have {s} dollars.")

print("=" * 24)
print(f"And there you have it, {s} dollars.")
while True:
    print("What's your name?")
    try:
        name = input()
        name_empty = len(name) == 0
    except EOFError:
        name_empty = True
    if not name_empty:
        break
    else:
        print("Please, enter something...")

print("Okay, we'll take notice.")
cur.execute("CREATE TABLE IF NOT EXISTS score(name, value)")
cur.execute("INSERT INTO score VALUES (?, ?)", (name, s))
con.commit()

print("=" * 24)
print("All scores:")
for score in cur.execute("SELECT * FROM score"):
    print(score)

con.close()
print("Goodbye!")
