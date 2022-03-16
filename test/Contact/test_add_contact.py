# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="First Contact", middlename="Middle Name", lastname="Last Name 1",
                      nickname="nickName1", title="Title1", company="Company1",
                      address="address1", home="Home1", mobile_phone="111222333", work_phone="Work1",
                      fax="111444555",
                      email="test@gmail.com",
                      homepage="homepage1", b_day="20", b_month="February", b_year="1900",
                      address_second="address2",
                      home_second="home1", notes="notes1")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
