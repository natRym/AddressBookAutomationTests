import pymysql.cursors

from model.contact import Contact
from model.group import Group


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute('select group_id, group_name, group_header, group_footer from group_list')
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3 from addressbook where deprecated ='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3) = row
                list.append(
                    Contact(id=str(id), firstname=firstname, lastname=lastname, address=address, home_phone=home,
                            mobile_phone=mobile, work_phone=work,
                            phone_secondary=phone2, email=email, email_second=email2, email_third=email3))
        finally:
            cursor.close()
        return list

    def get_contact_list_without_groups(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3 from addressbook where deprecated ='0000-00-00 00:00:00' and id not in (select id from address_in_groups)")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3) = row
                list.append(
                    Contact(id=str(id), firstname=firstname, lastname=lastname, address=address, home_phone=home,
                            mobile_phone=mobile, work_phone=work,
                            phone_secondary=phone2, email=email, email_second=email2, email_third=email3))
        finally:
            cursor.close()
        return list

    def get_group_list_with_contacts(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "SELECT group_id, group_name, group_header, group_footer FROM group_list WHERE deprecated ='0000-00-00 00:00:00' and `group_id` in (select group_id from address_in_groups)")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contacts_in_groups(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3 from addressbook where deprecated ='0000-00-00 00:00:00' and id in (select id from address_in_groups)")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3) = row
                list.append(
                    Contact(id=str(id), firstname=firstname, lastname=lastname, address=address, home_phone=home,
                            mobile_phone=mobile, work_phone=work,
                            phone_secondary=phone2, email=email, email_second=email2, email_third=email3))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
