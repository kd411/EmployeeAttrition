from cs50 import SQL
db = SQL("sqlite:///hr.db")
db.execute("CREATE TABLE login(id INTEGER PRIMARY KEY, username VARCHAR(20), password VARCHAR(20))")
db.execute("INSERT INTO login VALUES(1, 'ansh', '2299')")
db.execute("INSERT INTO login VALUES(2, 'kd', '1234')")
db.execute("INSERT INTO login VALUES(3, 'anay', 'khator')")
rows = db.execute("SELECT * FROM login")
for row in rows:
    print(row)
