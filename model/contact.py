from sys import maxsize


class Contact:

    def __init__(self, id=None, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None, address=None,
                 all_phones_from_home_page=None, home_phone=None, mobile_phone=None, work_phone=None, fax=None,
                 all_emails_from_home_page=None, email=None, email_second=None, email_third=None,
                 homepage=None, b_day=None, b_month=None, b_year=None, address_second=None, phone_secondary=None, notes=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.email = email
        self.email_second = email_second
        self.email_third = email_third
        self.homepage = homepage
        self.b_day = b_day
        self.b_month = b_month
        self.b_year = b_year
        self.address_second = address_second
        self.phone_secondary = phone_secondary
        self.notes = notes
        self.id = id
        self.all_emails_from_home_page = all_emails_from_home_page
        self.all_phones_from_home_page = all_phones_from_home_page

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
