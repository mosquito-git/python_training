from model.contact import Contact
# from random import randrange
import random
# import time


def test_edit_first_contact1(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test1", middlename="dfdfdf", lastname=""))
    old_contacts = db.get_contact_list()
    contact_rnd = random.choice(old_contacts)
    idx = old_contacts.index(contact_rnd)
    cont = Contact(firstname="task20", middlename="edit", lastname="contact",
                   nickname="edit", title="edit", company="mjyhy",
                   address="edit", home="812-555-44-33", mobile="+7-935-777-88-99",
                   work="567-78-99", fax="990-76-56", email="edit@edit.ru",
                   email2="edit@mail2.ru", email3="edit@mail3.ru",
                   homepage="www.edit.ru", bday="23", bmonth="May", byear="2010",
                   aday="9", amonth="April", ayear="1991", address2="edit",
                   phone2="11 12 13", notes="edit_notes_edit_notes_edit_notes")
    cont.id = contact_rnd.id
    app.contact.edit_contact_by_id(cont.id, cont)
    app.contact.return_to_home_page()
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[idx] = cont
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        new_contacts = app.contact.get_contact_list()
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#
# def test_edit_first_contact_firstname(app):
#     if app.contact.count() == 0:
#         app.contact.create(contact.Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
#                                            address="", home="", mobile="", work="", fax="", email="", email2="",
#                                            email3="", homepage="", bday="", bmonth="-", byear="", aday="", amonth="-",
#                                            ayear="", address2="", phone2="", notes=""))
#     app.contact.edit_first_contact(contact.Contact(firstname="new firstname"))
#     app.contact.return_to_home_page()
#
#
# def test_edit_first_contact_bday(app):
#     if app.contact.count() == 0:
#         app.contact.create(contact.Contact(firstname="test2", middlename="", lastname="test2"))
#     app.contact.edit_first_contact(contact.Contact(bday="11"))
#     app.contact.return_to_home_page()
#
#
# def test_edit_first_contact_amonth(app):
#     if app.contact.count() == 0:
#         app.contact.create(contact.Contact(firstname="test3", middlename="test3", lastname="test3"))
#     app.contact.edit_first_contact(contact.Contact(amonth="June"))
#     app.contact.return_to_home_page()
