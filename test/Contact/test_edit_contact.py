from model.contact import Contact
from random import randrange
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
    Contact(firstname=firstname, lastname=lastname, middlename=middlename,
            home_phone=home_phone)

    for firstname in [random_string_text_fields("firstname", 10)]
    for lastname in ["", random_string_text_fields("lastname", 20)]
    for middlename in ["", random_string_text_fields("middlename", 20)]
    for home_phone in [random_number_fields("+", 10)]
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_edit_some_contact(app, contact):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="First Contact"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_edit_page_opened_from_view_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="First Contact"))
    app.contact.open_edit_page_from_view_contact_page()


def test_edit_firstname_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="First Contact"))
    app.contact.edit_first_contact(Contact(firstname="edit firstname ONLY"))
