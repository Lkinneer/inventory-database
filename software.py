import sqlite3


def create_part(cursor, name):
    cursor.execute("INSERT INTO parts VALUES (3, '"+ name +"')")
def create_tables(cursor):
    c.execute('''CREATE TABLE parts(
    id int,
    name varchar(30) NOT NULL,
    PRIMARY KEY (id)
    );''')


conn = sqlite3.connect(':memory:')
#conn = sqlite3.connect('database.db')
c = conn.cursor()
create_tables(c)
c.execute("INSERT INTO parts VALUES (1, 'something'),(2, 'hing')")
create_part(c, "part name")
for row in c.execute("select name from parts"):
    print(row)

conn.commit()
conn.close()
#create table parts
'''
part id
part name
part description
part location
num part
'''


#create table shelve
'''
shelve id
shelve number
'''

#create table order
'''
order number
order id
date placed
date order fulfilled
'''

#create table partOrders
'''
parts requested
part id
order id
number
'''