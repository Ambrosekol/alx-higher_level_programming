#!/usr/bin/python3
"""
Write a script that lists all states from the database hbtn_0e_0_usa:

Your script should take 3 arguments: mysql username,
mysql password and database name (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported

"""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb
    
    user_name = argv[1]
    pswrd = argv[2]
    db_name = argv[3]
    
    db = MySQLdb.connect(host='localhost', port='3306', user=user_name,
                     passwd=pswrd, db=db_name)
    cursor = db.cursor()
    
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    resp = cursor.fetchall()
    