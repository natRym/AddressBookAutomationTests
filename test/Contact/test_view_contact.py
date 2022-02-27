def test_view_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.view_contact()
    app.session.logout()
