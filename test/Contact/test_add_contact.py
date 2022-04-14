# -*- coding: utf-8 -*-
import random

from model.contact import Contact
from model.group import Group


def test_add_contact(app, db, json_contacts):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_contact_is_added_into_group_via_grid(app, db, orm):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="First Contact"))
    if len(db.get_contact_list_without_groups()) == 0:
        app.contact.create(Contact(firstname="First Contact"))
    all_groups = db.get_group_list()
    group_for_adding = (random.choice(all_groups)).id
    contact_not_in_group = random.choice(orm.get_contacts_not_in_group(Group(id=group_for_adding)))
    contacts_in_group_before = orm.get_contacts_in_group(Group(id=group_for_adding))
    app.contact.add_contact_to_group_via_grid_by_id(contact_not_in_group.id, group_for_adding)
    contacts_in_group_after = orm.get_contacts_in_group(Group(id=group_for_adding))
    assert (len(contacts_in_group_after) == len(contacts_in_group_before) + 1)
    assert sorted(db.get_contacts_in_groups(), key=Contact.id_or_max) == sorted(db.get_contacts_in_groups(), key=Contact.id_or_max)
