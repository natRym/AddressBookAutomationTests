import re

from model.contact import Contact


def test_all_fields_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def test_all_fields_on_home_page_via_db(app, db, check_ui):
    contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

    def clean(contact):
        return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip(), address=contact.address.strip(),
                       email=contact.email.strip(), email_second=contact.email_second.strip(), email_third=contact.email_third.strip(),
                       home_phone=contact.home_phone.strip(), mobile_phone=contact.mobile_phone.strip(), work_phone=contact.work_phone.strip(),
                       phone_secondary=contact.phone_secondary.strip())

    contact_from_db = sorted(map(clean, db.get_contact_list()), key=Contact.id_or_max)
    for contact_ui, contact_db in zip(contact_from_home_page, contact_from_db):
        assert contact_ui.firstname == contact_db.firstname
        assert contact_ui.lastname == contact_db.lastname
        assert contact_ui.address == contact_db.address
        assert contact_ui.all_emails_from_home_page == merge_emails_like_on_home_page(contact_db)
        assert contact_ui.all_phones_from_home_page == merge_phones_like_on_home_page(contact_db)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone, contact.work_phone,
                                        contact.phone_secondary]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email, contact.email_second, contact.email_third])))
