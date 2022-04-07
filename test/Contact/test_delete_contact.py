from model.contact import Contact
import random

from model.group import Group


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


def test_delete_some_contact_from_edit_page(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="First Contact"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_from_edit_page(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


def test_contact_is_deleted_from_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test'))

    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="First Contact"))
    # db.get_contact_list().
    #    get_contacts_in_group()
    # group = random.choice(db.get_group_list())
    # contact_for_removing_from_group = random.choice(db.get_contact_list())
    # app.contact.delete_contact_from_group_via_grid_by_id(contact_for_removing_from_group.id, group.id)
    #db.get_contacts_not_in_group(Group(id=group.id))

