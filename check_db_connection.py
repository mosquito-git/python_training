import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='',
                             database='addressbook'
                             # cursorclass=pymysql.cursors.DictCursor
                             )

try:
    cursor = connection.cursor()
    cursor.execute("select * from group_list;")
    for row in cursor.fetchall():
        print(row)
finally:
    connection.commit()
    connection.close()