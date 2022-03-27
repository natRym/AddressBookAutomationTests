# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest
import random
import string


def random_string_text_fields(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_number_fields(prefix, maxlen):
    numbers = string.digits + " " * 10
    return prefix + "".join([random.choice(numbers) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(firstname=firstname, lastname=lastname,
            home_phone=home_phone)

    for firstname in ["", random_string_text_fields("firstname", 10)]
    for lastname in ["", random_string_text_fields("lastname", 20)]
    for home_phone in ["", random_number_fields("+", 10)]
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
