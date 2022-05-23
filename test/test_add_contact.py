# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
import random
import string
import re


def clear(s):
    return re.sub("[()\\ -'`]", "", s)


def rand_year():
    return "".join(
        random.choice(string.digits) + random.choice(string.digits) + random.choice(string.digits) + random.choice(
            string.digits))


def rand_month():
    month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                  'November', 'December']
    return random.choice(month_list)


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return clear(prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]))


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                    address="", home="", mobile="", work="", fax="", email="", email2="",
                    email3="", homepage="", bday="", bmonth="-", byear="", aday="", amonth="-",
                    ayear="", address2="", phone2="", notes="")] + [
               Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 20),
                       lastname=random_string("lastname", 20), nickname=random_string("nickname", 20),
                       title=random_string("title", 20), company=random_string("company", 20),
                       address=random_string("address", 20), home=random.randrange(1, 9),
                       mobile=random.randrange(1, 9), work=random.randrange(1, 9),
                       fax=random.randrange(1, 9), email=random_string("email", 5),
                       email2=random_string("email2", 5), email3=random_string("email3", 5),
                       homepage=random_string("homepage", 20),
                       # bday=random_string("bday", 20),
                       bday=str(random.randrange(1, 32)),
                       # bmonth="-",
                       bmonth=rand_month(),
                       # byear=random_string("byear", 20),
                       byear=rand_year(),
                       # aday=random_string("aday", 20),
                       aday=str(random.randrange(1, 32)),
                       # amonth="-",
                       amonth=rand_month(),
                       # ayear=random_string("ayear", 20),
                       ayear=rand_year(),
                       address2=random_string("address2", 20), phone2=random_string("phone2", 20),
                       notes=random_string("notes", 20))
               for i in range(5)
           ]


@pytest.mark.parametrize("cont", testdata, ids=[repr(x) for x in testdata])
def test_add_contact1(app, cont):
    old_contacts = app.contact.get_contact_list()
    # cont = Contact(firstname="aaaaa", middlename="bbbbb", middlename="ssssss",
    #                        nickname="hhhhhhhh", title="ddddddd", company="lsrhlrhg",
    #                        address="kshfu", home="812-555-44-33", mobile="+7-935-777-88-99",
    #                        work="567-78-99", fax="990-76-56", email="ckckc@mail.ru",
    #                        email2="wewe@mail2.ru", email3="wewrdd@mail3.ru",
    #                        homepage="www.hfhfhf.ru", bday="10", bmonth="May", byear="2000",
    #                        aday="3", amonth="April", ayear="1999", address2="sib",
    #                        phone2="45 45 54", notes="notesnotesnotes")
    app.contact.create(cont)
    app.contact.return_to_home_page()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(cont)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_add_empty_contact(app):
#     # app.session.login(username="admin", password="secret")
#     app.contact.create(contact.Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
#                                address="", home="", mobile="", work="", fax="", email="", email2="",
#                                email3="", homepage="", bday="", bmonth="-", byear="", aday="", amonth="-",
#                                ayear="", address2="", phone2="", notes=""))
#     app.contact.return_to_home_page()
#     # app.session.logout()
