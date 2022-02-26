from model.contact import Contact


def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit(Contact(firstname="Edit First Contact", middlename="Edit Middle Name", lastname="Edit Last Name 1",
                             nickname="Edit nickName1", title="Edit Title1", company="Edit Company1",
                             address="Edit address1", home="Edit Home1", mobile_phone="0111222333",
                             work_phone="EditWork1",
                             fax="0111444555",
                             email="Edit@gmail.com",
                             homepage="Edit homepage1", b_day="25", b_month="June", b_year="1950",
                             address_second="Edit address2",
                             home_second="Edit home1", notes="Edit notes1"))
    app.session.logout()


def test_edit_contact_to_empty_values(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit(Contact(firstname="", middlename="", lastname="",
                             nickname="", title="", company="",
                             address="", home="", mobile_phone="",
                             work_phone="",
                             fax="",
                             email="",
                             homepage="", b_day="-", b_month="-", b_year="-",
                             address_second="",
                             home_second="", notes=""))
    app.session.logout()
