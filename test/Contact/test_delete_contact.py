from model.contact import Contact
import random


def test_delete_some_contact_from_grid(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="First Contact"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


def test_delete_some_contact_from_edit_page(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="First Contact"))
    old_contacts = app.contact.get_contact_list()
    index = random.randrange(len(old_contacts))
    app.contact.delete_contact_from_edit_page(index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts


# def test_contact_is_deleted_from_group():

