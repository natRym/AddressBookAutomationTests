# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="First Contact", middlename="Middle Name", lastname="Last Name 1",
                      nickname="nickName1", title="Title1", company="Company1",
                      address="address1", home_phone="111222333", mobile_phone="22334444444", work_phone="333334444444",
                      fax="111444555",
                      email="test@gmail.com",
                      homepage="homepage1", b_day="20", b_month="February", b_year="1900",
                      address_second="address2",
                      phone_secondary="55555555555555", notes="notes1")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
