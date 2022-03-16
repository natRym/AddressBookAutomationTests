from model.contact import Contact


def test_edit_first_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Edit First Contact", middlename="Edit Middle Name", lastname="Edit Last Name 1",
                      nickname="Edit nickName1", title="Edit Title1", company="Edit Company1",
                      address="Edit address1", home="Edit Home1", mobile_phone="0111222333",
                      work_phone="EditWork1",
                      fax="0111444555",
                      email="Edit@gmail.com",
                      homepage="Edit homepage1", b_day="25", b_month="June", b_year="1950",
                      address_second="Edit address2",
                      home_second="Edit home1", notes="Edit notes1")
    contact.id = old_contacts[0].id
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="First Contact"))
    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#
# def test_edit_first_contact_to_empty_values(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="First Contact"))
#     app.contact.edit_first_contact(Contact(firstname="", middlename="", lastname="",
#                                            nickname="", title="", company="",
#                                            address="", home="", mobile_phone="",
#                                            work_phone="",
#                                            fax="",
#                                            email="",
#                                            homepage="", b_day="-", b_month="-", b_year="-",
#                                            address_second="",
#                                            home_second="", notes=""))
#
#
# def test_edit_page_opened_from_view_contact(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="First Contact"))
#     app.contact.edit_page_from_view_contact()
#
#
# def test_edit_firstname_first_contact(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="First Contact"))
#     app.contact.edit_first_contact(Contact(firstname="edit firstname ONLY"))
