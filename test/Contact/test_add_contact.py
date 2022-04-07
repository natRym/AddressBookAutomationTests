# -*- coding: utf-8 -*-
import random

from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture

# dataBase = ORMFixture(host='127.0.0.1', name='addressbook', user='root', password='')


def test_add_contact(app, db, json_contacts):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_contact_is_added_into_group_via_grid(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="First Contact"))
    contacts_before_adding = random.choice(db.get_contact_list())
    groups_before_adding = random.choice(db.get_group_list())
    app.contact.add_contact_to_group_via_grid_by_id(contacts_before_adding.id, groups_before_adding.id)
    groups_after_adding = ORMFixture.select().limit(5)
    print(groups_after_adding)

