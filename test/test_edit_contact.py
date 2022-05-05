from model import contact


def test_edit_first_contact1(app):
    if app.contact.count() == 0:
        app.contact.create(contact.Contact(firstname="test1", middlename="dfdfdf", lastname=""))
    app.contact.edit_first_contact(contact.Contact(firstname="edit", middlename="contact", lastname="edit",
                                                   nickname="edit", title="edit", company="edit",
                                                   address="edit", home="812-555-44-33", mobile="+7-935-777-88-99",
                                                   work="567-78-99", fax="990-76-56", email="edit@edit.ru",
                                                   email2="edit@mail2.ru", email3="edit@mail3.ru",
                                                   homepage="www.edit.ru", bday="23", bmonth="May", byear="2010",
                                                   aday="9", amonth="April", ayear="1991", address2="edit",
                                                   phone2="www.edit2.ru", notes="edit_notes_edit_notes_edit_notes"))
    app.contact.return_to_home_page()


def test_edit_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(contact.Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                                           address="", home="", mobile="", work="", fax="", email="", email2="",
                                           email3="", homepage="", bday="", bmonth="-", byear="", aday="", amonth="-",
                                           ayear="", address2="", phone2="", notes=""))
    app.contact.edit_first_contact(contact.Contact(firstname="new firstname"))
    app.contact.return_to_home_page()


def test_edit_first_contact_bday(app):
    if app.contact.count() == 0:
        app.contact.create(contact.Contact(firstname="test2", middlename="", lastname="test2"))
    app.contact.edit_first_contact(contact.Contact(bday="11"))
    app.contact.return_to_home_page()


def test_edit_first_contact_amonth(app):
    if app.contact.count() == 0:
        app.contact.create(contact.Contact(firstname="test3", middlename="test3", lastname="test3"))
    app.contact.edit_first_contact(contact.Contact(amonth="June"))
    app.contact.return_to_home_page()
