from selenium.webdriver.support.select import Select

from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contacts_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/")):
            wd.find_element_by_link_text("home").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_add_contact_page()
        # init opening add contact page
        self.fill_contact_form(contact)
        # submit changes
        wd.find_element_by_xpath("//input[@type='submit']").click()
        self.contact_cache = None

    def open_add_contact_page(self):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()

    def open_contact_view_page_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def open_contact_edit_page_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_edit_page_by_id(self, id):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element_by_xpath("//a[@href='edit.php?id=%s']" % id).click()

    def open_contact_view_page_by_id(self, id):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element_by_xpath("//a[@href='view.php?id=%s']" % id).click()

    def fill_contact_form(self, contact):
        self.change_contact_field_value("firstname", contact.firstname)
        self.change_contact_field_value("middlename", contact.middlename)
        self.change_contact_field_value("lastname", contact.lastname)
        self.change_contact_field_value("nickname", contact.nickname)
        self.change_contact_field_value("title", contact.title)
        self.change_contact_field_value("company", contact.company)
        self.change_contact_field_value("address", contact.address)
        self.change_contact_field_value("home", contact.home_phone)
        self.change_contact_field_value("mobile", contact.mobile_phone)
        self.change_contact_field_value("work", contact.work_phone)
        self.change_contact_field_value("fax", contact.fax)
        self.change_contact_field_value("email", contact.email)
        self.change_contact_field_value("homepage", contact.homepage)
        self.change_drop_down_value("bday", contact.b_day)
        self.change_drop_down_value("bmonth", contact.b_month)
        self.change_contact_field_value("byear", contact.b_year)
        self.change_contact_field_value("address2", contact.address_second)
        self.change_contact_field_value("phone2", contact.phone_secondary)
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
        self.open_contacts_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def edit_first_contact(self, new_contact_data):
        self.edit_contact_by_index(0, new_contact_data)

    def edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_contact_edit_page_by_index(index)
        # wd.find_element_by_name("Edit / add address book entry")
        self.fill_contact_form(new_contact_data)
        # init submission changes
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def edit_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.open_contact_edit_page_by_id(id)
        # wd.find_element_by_name("Edit / add address book entry")
        self.fill_contact_form(new_contact_data)
        # init submission changes
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def open_edit_page_from_view_contact_page(self):
        wd = self.app.wd
        # init opening contacts page
        self.open_contacts_page()
        # open a contact to view details
        wd.find_element_by_xpath("//img[@title='Details']").click()
        # init edition of a contact
        wd.find_element_by_name("modifiy").click()

    def detect_edit_page_is_active(self):
        wd = self.app.wd
        self.open_edit_page_from_view_contact_page()
        wd.find_element_by_xpath("//div[@id='content']/h1[text()='Edit / add address book entry']")

    def detect_view_page_is_active(self, id):
        wd = self.app.wd
        self.open_contact_view_page_by_id(id)
        wd.find_element_by_xpath("//form[@action='view.php']/input[@name='print']")

    def delete_first_contact(self):
        self.delete_contact_from_grid_by_index(0)

    def delete_contact_from_grid_by_index(self, index):
        wd = self.app.wd
        # init opening contacts page
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        wd.find_element_by_xpath("//div[@class='msgbox']")
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        # init opening contacts page
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        wd.find_element_by_xpath("//div[@class='msgbox']")
        self.contact_cache = None

    def delete_contact_from_edit_page(self, id):
        wd = self.app.wd
        self.open_contact_edit_page_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.find_element_by_xpath("//table[@id='maintable']")
        self.contact_cache = None

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
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                id = element.find_element_by_name("selected[]").get_attribute("value")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails,
                                                  address=address))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_edit_page_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        phone_secondary = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email_second = wd.find_element_by_name("email2").get_attribute("value")
        email_third = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(lastname=lastname, firstname=firstname, id=id,
                       home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone,
                       phone_secondary=phone_secondary, address=address, email=email, email_second=email_second,
                       email_third=email_third)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_page_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        phone_secondary = re.search("P: (.*)", text).group(1)
        return Contact(home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone,
                       phone_secondary=phone_secondary)

    def add_contact_to_group_via_grid_by_id(self, contact_id, group_id):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_id(contact_id)
        wd.find_element_by_name("to_group").click()
        Select(wd.find_element_by_name("to_group")).select_by_value(group_id)
        wd.find_element_by_name("add").click()
        self.open_contacts_page()
        self.contact_cache = None


