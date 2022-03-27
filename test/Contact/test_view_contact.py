from random import randrange

from model.contact import Contact


def test_view_any_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="First Contact"))
    contact_list = app.contact.get_contact_list()
    index = randrange(len(contact_list))
    app.contact.open_contact_view_page_by_index(index)
