from random import randrange
from model.contact import Contact
import re


def test_data_on_home_page_and_from_db(app, db):
    contacts_from_home_page = app.contact.get_contact_list()
    contact_from_db = db.get_contact_list()
    # print('some_contacts_from_home_page=',contacts_from_home_page)
    # print('contact_from_db=', contact_from_db)
    assert sorted(contacts_from_home_page, key=Contact.id_or_max) == sorted(contact_from_db, key=Contact.id_or_max)



def test_data_on_home_page(app):
    some_contacts_from_home_page = app.contact.get_contact_list()
    index = randrange(len(some_contacts_from_home_page))
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert some_contacts_from_home_page[index].firstname == contact_from_edit_page.firstname
    assert some_contacts_from_home_page[index].lastname == contact_from_edit_page.lastname
    assert some_contacts_from_home_page[index].address == contact_from_edit_page.address
    assert some_contacts_from_home_page[index].all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert merge_emails(some_contacts_from_home_page[index].all_emails_from_home_page) == merge_emails([contact_from_edit_page.email, contact_from_edit_page.email2, contact_from_edit_page.email3])


#
def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [contact.home,
                                                                                                        contact.mobile,
                                                                                                        contact.work,
                                                                                                        contact.phone2]))))


def merge_emails(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, contact))))
