from model import contact
import time


def test_del_contact1(app):
    if app.contact.count() == 0:
        app.contact.create(contact.Contact(firstname="gggggg", middlename="dfdfdf", lastname="dfffff"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    time.sleep(1)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
