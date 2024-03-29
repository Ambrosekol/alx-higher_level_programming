#!/usr/bin/python3
"""
Script that lists all states from the database
This is based on the ALX SE program
Write a script that takes in an argument and
displays all values in the states table of
hbtn_0e_0_usa where name matches the argument
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    cont = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        password=argv[2], database=argv[3])
    cursor = cont.cursor()
    cursor.execute(
            "SELECT * FROM states WHERE name LIKE"
            " '{:s}' ORDER BY id ASC".format(argv[4]))
    db = cursor.fetchall()
    for i in db:
        if i[1] == argv[4]:
            print(i)
