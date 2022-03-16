from selenium.webdriver.support.select import Select

from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_contact_page(self):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()

    def open_contacts_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/")):
            wd.find_element_by_link_text("home").click()

    def create(self, contact):
        # init opening add contact page
        wd = self.app.wd
        self.open_add_contact_page()
        self.fill_contact_form(contact)
        # submit changes
        wd.find_element_by_xpath("//input[@type='submit']").click()

    def fill_contact_form(self, contact):
        self.change_contact_field_value("firstname", contact.firstname)
        self.change_contact_field_value("middlename", contact.middlename)
        self.change_contact_field_value("lastname", contact.lastname)
        self.change_contact_field_value("nickname", contact.nickname)
        self.change_contact_field_value("title", contact.title)
        self.change_contact_field_value("company", contact.company)
        self.change_contact_field_value("address", contact.address)
        self.change_contact_field_value("home", contact.home)
        self.change_contact_field_value("mobile", contact.mobile_phone)
        self.change_contact_field_value("work", contact.work_phone)
        self.change_contact_field_value("fax", contact.fax)
        self.change_contact_field_value("email", contact.email)
        self.change_contact_field_value("homepage", contact.homepage)
        self.change_drop_down_value("bday", contact.b_day)
        self.change_drop_down_value("bmonth", contact.b_month)
        self.change_contact_field_value("byear", contact.b_year)
        self.change_contact_field_value("address2", contact.address_second)
        self.change_contact_field_value("phone2", contact.home_second)
        self.change_contact_field_value("notes", contact.notes)

    def change_contact_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_drop_down_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)
            wd.find_element_by_xpath("//option[@value='%s']" % text).click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()

    def edit_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.select_contact_by_index(0)

    def edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        # init opening contacts page
        self.open_contacts_page()
        self.select_contact_by_index(index)
        # wd.find_element_by_name("Edit / add address book entry")
        self.fill_contact_form(new_contact_data)
        # init submission changes
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def edit_page_from_view_contact(self):
        wd = self.app.wd
        # init opening contacts page
        self.open_contacts_page()
        # open a contact to view details
        wd.find_element_by_xpath("//img[@title='Details']").click()
        # init edition of a contact
        wd.find_element_by_name("modifiy").click()

    def delete_first_contact(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        # init opening contacts page
        self.open_contacts_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
  #      wd.switch_to.alert.accept()
        wd.find_element_by_xpath("//div[@class='msgbox']")
        self.contact_cache = None

    def delete_contact_from_edit_page(self, index):
        wd = self.app.wd
        # init opening contacts page
        self.open_contacts_page()
        self.edit_contact_by_index()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.find_element_by_xpath("//table[@id='maintable']")

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contact_cache = []
            rows_quantity = len(wd.find_elements_by_css_selector("table tbody tr[name*='entry']"))
            for row_number in range(rows_quantity):
                row_elements = wd.find_elements_by_css_selector("table tbody tr[name*='entry']:nth-child(%d) td" % (row_number + 2))
                self.contact_cache.append(Contact(id=(row_number + 1), firstname=row_elements[2].text, lastname=row_elements[1].text))
        return list(self.contact_cache)
