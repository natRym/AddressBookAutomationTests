def test_delete_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_contact()
    app.session.logout()


def test_test_delete_contact_from_edit_page(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_contact_from_edit_page()
    app.session.logout()
