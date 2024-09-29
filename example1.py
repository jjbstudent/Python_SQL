#example of using SQL and python

import sqlite3

connection = sqlite3.connect("mydb.db")

cursor = connection.cursor()


def makeTable():
    #Make the database table if it does not exist 
    #the SQl will make a table called main, add an id, name and colour field
    command1 = "CREATE TABLE IF NOT EXISTS main(id INTEGER PRIMARY KEY, name TEXT, colour TEXT)"
    cursor.execute(command1)

    #add values into the table
    cursor.execute("INSERT INTO main VALUES (1, 'Mario', 'Red')")
    cursor.execute("INSERT INTO main VALUES (2, 'Luigi', 'Green')")
    cursor.execute("INSERT INTO main VALUES (3, 'Bowser', 'Purple')")
    cursor.execute("INSERT INTO main VALUES (4, 'Wario', 'Yellow')")

    #make the data permanent
    connection.commit()

#run the function to make the table
makeTable()