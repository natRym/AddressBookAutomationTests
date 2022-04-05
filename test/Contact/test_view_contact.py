import random

from model.contact import Contact


def test_view_any_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="First Contact"))
    contact = random.choice(db.get_contact_list())
    app.contact.open_contact_view_page_by_id(contact.id)
    assert (app.contact.detect_view_page_is_active(contact.id), "View Page is NOT Opened")
