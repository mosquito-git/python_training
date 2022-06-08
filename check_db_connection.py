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
    # sql = "select * from group_list;"
    sql = "select id,firstname,middlename,lastname from addressbook"
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)
finally:
    connection.commit()
    connection.close()