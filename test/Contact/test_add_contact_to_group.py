import random

from model.contact import Contact
from model.group import Group


def test_contact_is_added_into_group_via_grid(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="First Contact"))
    contact_for_adding_to_group = random.choice(db.get_contact_list())
    group_for_contact = random.choice(db.get_group_list())
    app.contact.add_contact_to_group_via_grid_by_id(contact_for_adding_to_group.id, group_for_contact.id)
    db.get_contacts_in_group(Group(id=group_for_contact.id))
