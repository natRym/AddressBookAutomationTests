# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="First Contact", middlename="Middle Name", lastname="Last Name 1",
                               nickname="nickName1", title="Title1", company="Company1",
                               address="address1", home="Home1", mobile_phone="111222333", work_phone="Work1",
                               fax="111444555",
                               email="test@gmail.com",
                               homepage="homepage1", b_day="20", b_month="February", b_year="1900",
                               address_second="address2",
                               home_second="home1", notes="notes1"))
    app.session.logout()

