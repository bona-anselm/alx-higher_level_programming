# Python - Object-relational mapping
------------------------------------

We were yet again introduced into another concept, this time Object Relational Mapping in Python. This concept teaches us the possibilty in accessing information stored in a database directly from python. Here, we concentrated on using ```MySQLdb``` and/or ```SQLAlchemy``` to perform any of the CRUD functions in database management.

This project involves the following concepts, languages and/or frameworks: Python, OOP, SQL, MySQL, ORM, SQLAlchemy.

##### This concept without ORM
```
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```

##### This same concept with ORM
```
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
```

### General Learning Objectives
--------------------------------

- Why Python programming is awesome
- How to connect to a MySQL database from a Python script
- How to ```SELECT``` rows in a MySQL table from a Python script
- How to ```INSERT``` rows in a MySQL table from a Python script
- What ORM means
- How to map a Python Class to a MySQL table


