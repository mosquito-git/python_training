import pymysql.cursors
from fixture.db import DbFixture

# Connect to the database
# connection = pymysql.connect(host='127.0.0.1',
#                              user='root',
#                              password='',
#                              database='addressbook'
#                              # cursorclass=pymysql.cursors.DictCursor
#                              )
db = DbFixture(host='127.0.0.1', user='root', password='', name='addressbook')

try:
    # groups = db.get_group_list()
    # for group in groups:
    #     print(group)
    # print(len(groups))
    contacts = db.get_contact_list()
    for contact in contacts:
        print(contact)
    print(len(contacts))
finally:
    db.destroy()