import pymysql

from fixture.db import DbFixture
from fixture.orm import ORMFixture
from model.group import Group

# db = ORMFixture(host='127.0.0.1', name='addressbook', user='root', password='')
#
# try:
#     l = db.get_group_list_with_contacts(Group(id='277'))
#     for item in l:
#         print(item)
#     print(len(l))
# finally:
#     pass  # db.destroy()


db = DbFixture(host='127.0.0.1', name='addressbook', user='root', password='')

try:
    l = db.get_contact_added_to_group()
    # for item in l:
    #     print(item)
    # print(len(l))
    print(l)
finally:
    pass  # db.destroy()

