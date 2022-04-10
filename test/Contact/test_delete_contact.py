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


def test_contact_is_deleted_from_group(app, db, orm):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="First Contact"))
    group_list_with_contacts = db.get_group_list_with_contacts()
    group_for_remove_contact = (random.choice(group_list_with_contacts)).id
    contacts_in_group_before = orm.get_contacts_in_group(Group(id=group_for_remove_contact))
    contact_id_to_delete_from_group = random.choice(contacts_in_group_before).id
    app.contact.delete_contact_from_group_via_grid_by_id(contact_id_to_delete_from_group, group_for_remove_contact)
    contacts_in_group_after = orm.get_contacts_in_group(Group(id=group_for_remove_contact))
    assert (len(contacts_in_group_before) - 1 == len(contacts_in_group_after))
    assert sorted(db.get_contacts_before_adding_to_group(), key=Contact.id_or_max) == sorted(db.get_contacts_after_adding_to_group(), key=Contact.id_or_max)
