import pymysql.cursors
from fixture.orm import ORMFixture
from model.group import Group

# Connect to the database
# connection = pymysql.connect(host='127.0.0.1',
#                              user='root',
#                              password='',
#                              database='addressbook'
#                              # cursorclass=pymysql.cursors.DictCursor
#                              )
db = ORMFixture(host='127.0.0.1', user='root', password='', name='addressbook')

try:
    # groups = db.get_group_list()
    # for group in groups:
    #     print(group)
    # print(len(groups))
    l = db.get_contacts_in_group(Group(id='104'))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass  # db.destroy()
