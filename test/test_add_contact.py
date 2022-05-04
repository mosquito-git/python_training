# -*- coding: utf-8 -*-

from model import contact


def test_add_contact1(app):
    # app.session.login(username="admin", password="secret")
    app.contact.create(contact.Contact(firstname="aaaaa", middlename="bbbbb", lastname="ssssss",
                               nickname="hhhhhhhh", title="ddddddd", company="lsrhlrhg",
                               address="kshfu", home="812-555-44-33", mobile="+7-935-777-88-99",
                               work="567-78-99", fax="990-76-56", email="ckckc@mail.ru",
                               email2="wewe@mail2.ru", email3="wewrdd@mail3.ru",
                               homepage="www.hfhfhf.ru", bday="10", bmonth="May", byear="2000",
                               aday="3", amonth="April", ayear="1999", address2="sib",
                               phone2="www.home2.ru", notes="notesnotesnotes"))
    app.contact.return_to_home_page()
    # app.session.logout()


def test_add_empty_contact(app):
    # app.session.login(username="admin", password="secret")
    app.contact.create(contact.Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                               address="", home="", mobile="", work="", fax="", email="", email2="",
                               email3="", homepage="", bday="", bmonth="-", byear="", aday="", amonth="-",
                               ayear="", address2="", phone2="", notes=""))
    app.contact.return_to_home_page()
    # app.session.logout()